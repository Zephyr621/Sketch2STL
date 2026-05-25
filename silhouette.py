"""从 STL 或二值草图提取用于匹配的轮廓特征。"""
import struct
from pathlib import Path
from typing import Optional

import cv2
import numpy as np


def read_stl_vertices(stl_path: Path) -> Optional[np.ndarray]:
    """读取 STL 顶点（支持 binary；ascii 尝试简易解析）。"""
    data = stl_path.read_bytes()
    if len(data) < 84:
        return None

    if data[:5].lower() == b"solid":
        return _read_stl_ascii(data.decode("utf-8", errors="ignore"))

    try:
        tri_count = struct.unpack("<I", data[80:84])[0]
        expected = 84 + tri_count * 50
        if expected > len(data):
            return None
        verts = []
        offset = 84
        for _ in range(tri_count):
            offset += 12  # normal
            for _ in range(3):
                verts.append(struct.unpack("<fff", data[offset : offset + 12]))
                offset += 12
            offset += 2
        return np.array(verts, dtype=np.float64)
    except struct.error:
        return None


def _read_stl_ascii(text: str) -> Optional[np.ndarray]:
    verts = []
    for line in text.splitlines():
        line = line.strip().lower()
        if line.startswith("vertex"):
            parts = line.split()
            if len(parts) >= 4:
                verts.append([float(parts[1]), float(parts[2]), float(parts[3])])
    if not verts:
        return None
    return np.array(verts, dtype=np.float64)


def vertices_to_contour(vertices: np.ndarray, plane: str = "xy") -> Optional[np.ndarray]:
    """将 3D 顶点投影为 2D 轮廓（凸包）。"""
    if vertices is None or len(vertices) < 3:
        return None
    if plane == "xy":
        pts = vertices[:, :2]
    elif plane == "xz":
        pts = vertices[:, [0, 2]]
    else:
        pts = vertices[:, 1:3]

    pts = pts.astype(np.float32)
    pts = pts - pts.mean(axis=0)
    scale = float(np.max(np.abs(pts))) or 1.0
    pts = (pts / scale) * 200.0

    hull = cv2.convexHull(pts.reshape(-1, 1, 2))
    if hull is None or len(hull) < 3:
        return None
    return hull


def extract_main_contour(binary_image: np.ndarray, min_area: float = 500) -> Optional[np.ndarray]:
    """提取最大轮廓（保留图像坐标，用于预览绘制）。"""
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    main = max(contours, key=cv2.contourArea)
    if cv2.contourArea(main) < min_area:
        return None
    if main is None or len(main) < 3:
        return None
    return main


def binary_to_main_contour(binary_image: np.ndarray) -> Optional[np.ndarray]:
    """提取并归一化轮廓（用于与模板匹配）。"""
    main = extract_main_contour(binary_image)
    if main is None:
        return None
    return normalize_contour(main)


def normalize_contour(contour: np.ndarray) -> Optional[np.ndarray]:
    """平移、缩放轮廓，使草图与 STL 投影在同一尺度下比较。"""
    if contour is None or len(contour) < 3:
        return None
    c = contour.astype(np.float32).reshape(-1, 2)
    if len(c) < 3:
        return None
    M = cv2.moments(c.reshape(-1, 1, 2))
    if abs(M["m00"]) < 1e-6:
        return contour.astype(np.float32)
    cx = M["m10"] / M["m00"]
    cy = M["m01"] / M["m00"]
    c = c - np.array([cx, cy], dtype=np.float32)
    scale = float(np.max(np.linalg.norm(c, axis=1)))
    if scale < 1e-6:
        scale = 1.0
    c = (c / scale) * 200.0
    out = c.reshape(-1, 1, 2).astype(np.float32)
    return out if len(out) >= 3 else None


def contour_match_score(contour_a: np.ndarray, contour_b: np.ndarray) -> float:
    """OpenCV 轮廓匹配，越小越相似。多种度量取最小值。"""
    a = normalize_contour(contour_a)
    b = normalize_contour(contour_b)
    if a is None or b is None:
        return 999.0
    scores = []
    for method in (
        cv2.CONTOURS_MATCH_I1,
        cv2.CONTOURS_MATCH_I2,
        cv2.CONTOURS_MATCH_I3,
    ):
        try:
            scores.append(float(cv2.matchShapes(a, b, method, 0.0)))
        except cv2.error:
            continue
    return min(scores) if scores else 999.0


def stl_to_contour(stl_path: Path) -> Optional[np.ndarray]:
    """取 STL 三向投影中轮廓面积最大的凸包（与手绘正视图更一致）。"""
    verts = read_stl_vertices(stl_path)
    if verts is None:
        return None
    best = None
    best_area = 0.0
    for plane in ("xy", "xz", "yz"):
        c = vertices_to_contour(verts, plane)
        if c is None:
            continue
        area = cv2.contourArea(c)
        if area > best_area:
            best_area = area
            best = c
    if best is None:
        return None
    return normalize_contour(best)
