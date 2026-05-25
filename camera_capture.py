import argparse
import math
import shutil
import sys
from pathlib import Path
from typing import Optional

import cv2
import numpy as np

from config import (
    FIXED_CODE_DIR,
    INDEX_PATH,
    OUTPUT_DIR,
    PROJECT_ROOT,
    RETRIEVAL_MAX_SCORE,
)
from primitives import generate_primitive_stl
from retrieval import TemplateRetriever
from silhouette import binary_to_main_contour, extract_main_contour
from template_runner import run_template

# ==================== 路径配置（兼容旧引用） ====================
DATA_DIR = PROJECT_ROOT / "data"


class CameraSketchToCadQuery:
    """摄像头草图 → 模板检索 / 基本体回退 → STL"""

    def __init__(self):
        self.cap = None
        self.retriever = TemplateRetriever()
        self._index_ready = False
        self._check_index()

    def _check_index(self):
        if self.retriever.available:
            n = self.retriever.load()
            self._index_ready = n > 0
            print(f"已加载模板检索索引: {n} 个可匹配模板")
        else:
            print("提示: 尚未构建模板索引，将使用基本体回退。")
            print("      请运行: python build_template_index.py")
            print("      或:     python camera_capture.py --build-index")

    def open_camera(self):
        for camera_id in [0, 1]:
            backends = [
                (cv2.CAP_DSHOW, "DSHOW"),
                (cv2.CAP_MSMF, "MSMF"),
                (cv2.CAP_ANY, "ANY"),
            ]
            for backend, backend_name in backends:
                try:
                    cap = cv2.VideoCapture(camera_id, backend)
                    if cap.isOpened():
                        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        print(f"成功打开摄像头 {camera_id} (后端: {backend_name})")
                        return cap
                except Exception:
                    continue
        return None

    def capture_from_camera(self):
        self.cap = self.open_camera()
        if self.cap is None:
            print("\n" + "=" * 50)
            print("【错误】无法打开摄像头！")
            print("=" * 50)
            print("\n请尝试: 关闭占用摄像头的程序 / 检查系统权限")
            print("\n也可使用本地图片: python camera_capture.py --image your_sketch.jpg")
            input("\n按回车键退出...")
            return None

        print("\n摄像头已打开！")
        print("在绿色框内绘制草图")
        print("按 [空格] 拍照识别 | [ESC] 退出\n")

        for _ in range(10):
            self.cap.read()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            margin = 80
            draw_area = (margin, margin, w - 2 * margin, h - 2 * margin)

            cv2.rectangle(
                frame,
                (draw_area[0], draw_area[1]),
                (draw_area[0] + draw_area[2], draw_area[1] + draw_area[3]),
                (0, 255, 0),
                3,
            )
            cv2.putText(
                frame,
                "SKETCH TO STL",
                (w // 2 - 100, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                frame,
                "SPACE: Capture | ESC: Exit",
                (w // 2 - 150, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (200, 200, 200),
                1,
            )
            cv2.imshow("Sketch Capture", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                return None
            if key == 32:
                sketch = frame[
                    draw_area[1] : draw_area[1] + draw_area[3],
                    draw_area[0] : draw_area[0] + draw_area[2],
                ]
                cv2.imwrite(str(OUTPUT_DIR / "captured_raw.jpg"), sketch)
                print("\n已捕获图像，正在处理...")
                return sketch
        return None

    def load_image(self, image_path: Path):
        img = cv2.imread(str(image_path))
        if img is None:
            print(f"无法读取图片: {image_path}")
            return None
        cv2.imwrite(str(OUTPUT_DIR / "captured_raw.jpg"), img)
        print(f"已加载图片: {image_path}")
        return img

    def preprocess_sketch(self, image):
        print("  - 灰度与二值化...")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        binary = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            11,
            2,
        )
        kernel = np.ones((3, 3), np.uint8)
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        denoised = cv2.medianBlur(closed, 3)
        cv2.imwrite(str(OUTPUT_DIR / "processed_binary.jpg"), denoised)
        return denoised

    def draw_contour_preview(self, image, binary):
        preview = image.copy()
        contour = extract_main_contour(binary)
        if contour is not None and len(contour) >= 3:
            cv2.drawContours(preview, [contour.astype(np.int32)], -1, (0, 255, 0), 2)
        cv2.imwrite(str(OUTPUT_DIR / "contour_preview.jpg"), preview)

    def analyze_shape_fallback(self, binary_image):
        """检索失败时的基本体分类（保留原逻辑）。"""
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None, None

        main_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(main_contour)
        if area < 500:
            return None, None

        perimeter = cv2.arcLength(main_contour, True)
        approx = cv2.approxPolyDP(main_contour, 0.02 * perimeter, True)
        num_vertices = len(approx)
        rect = cv2.minAreaRect(main_contour)
        (_, _), (width, height), _ = rect
        if width < height:
            width, height = height, width

        circularity = (4 * math.pi * area / (perimeter * perimeter)) if perimeter > 0 else 0

        if circularity > 0.7 and num_vertices > 8:
            shape_type = "sphere"
        elif num_vertices == 4:
            aspect = width / height if height > 0 else 1
            shape_type = "cube" if 0.8 < aspect < 1.2 else "rectangle"
        elif num_vertices == 3:
            shape_type = "cone"
        elif 5 <= num_vertices <= 8 and circularity > 0.6:
            shape_type = "cylinder"
        else:
            shape_type = "cube"

        size = max(5, min(50, math.sqrt(area) / 5))
        return shape_type, {"size": size, "width": width, "height": height}

    def export_from_template(self, match: dict) -> Optional[Path]:
        template_id = match["id"]
        score = match.get("score", 0)
        out_stl = OUTPUT_DIR / f"matched_{template_id}.stl"
        out_py = OUTPUT_DIR / f"matched_{template_id}.py"

        print(f"  匹配模板 #{template_id} (分数 {score:.4f}, 越小越好)")

        code_path = PROJECT_ROOT / match["code_path"]
        if code_path.exists():
            shutil.copy2(code_path, out_py)

        if match.get("has_stl") and match.get("stl_path"):
            stl_src = PROJECT_ROOT / match["stl_path"]
            if stl_src.exists():
                shutil.copy2(stl_src, out_stl)
                print(f"  已从模板库复制 STL: {out_stl}")
                return out_stl

        if match.get("syntax_ok") and code_path.exists():
            print("  正在执行 CadQuery 模板生成 STL...")
            ok, err = run_template(code_path, out_stl)
            if ok:
                print(f"  已生成 STL: {out_stl}")
                return out_stl
            print(f"  模板执行失败: {err}")

        return None

    def process_sketch(self, sketch) -> Optional[Path]:
        binary = self.preprocess_sketch(sketch)
        self.draw_contour_preview(sketch, binary)

        print("\n【步骤3】模板检索")
        print("-" * 40)

        if self._index_ready:
            matches = self.retriever.search(binary)
            for i, m in enumerate(matches, 1):
                print(f"  Top{i}: 模板 {m['id']}  分数 {m['score']:.4f}")

            if matches and self.retriever.should_accept_match(matches):
                best = matches[0]
                print(f"  采用模板 {best['id']} (分数 {best['score']:.4f})")
                stl = self.export_from_template(best)
                if stl:
                    return stl
            elif matches:
                print(
                    f"  最佳分数 {matches[0]['score']:.4f} 未达阈值 "
                    f"(需 <= {RETRIEVAL_MAX_SCORE} 或 Top1/Top2 差距明显)"
                )
            print("  回退到基本体生成...")
        else:
            print("  索引未就绪，回退到基本体生成...")

        print("\n【步骤3b】基本体识别")
        print("-" * 40)
        shape_type, params = self.analyze_shape_fallback(binary)
        if shape_type is None:
            print("\n未能识别形状，请确保轮廓清晰且在框内。")
            return None

        print(f"  基本体类型: {shape_type}")
        print("\n【步骤4】生成 STL")
        print("-" * 40)
        stl_path, _ = generate_primitive_stl(shape_type, params)
        print(f"  STL: {stl_path}")
        return stl_path

    def run(self, image_path: Optional[Path] = None):
        print("\n" + "=" * 60)
        print("    摄像头草图 → STL（模板检索 + 基本体回退）")
        print("=" * 60)
        print(f"输出目录: {OUTPUT_DIR}")
        print("=" * 60)

        if image_path:
            print("\n【步骤1】加载图片")
            sketch = self.load_image(image_path)
        else:
            print("\n【步骤1】摄像头采集")
            sketch = self.capture_from_camera()

        if sketch is None:
            print("\n已退出")
            return

        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()

        print("\n【步骤2】图像预处理")
        print("-" * 40)
        stl_path = self.process_sketch(sketch)

        if stl_path is None:
            return

        print("\n" + "=" * 60)
        print("处理完成")
        print(f"STL: {stl_path}")
        print("=" * 60)

        try:
            import os

            os.startfile(str(stl_path))
            print("\n已尝试用系统默认程序打开 STL")
        except Exception:
            print(f"\n请手动打开: {stl_path}")


def main():
    parser = argparse.ArgumentParser(description="Sketch2STL 草图转 3D")
    parser.add_argument("--image", "-i", type=Path, help="使用本地图片代替摄像头")
    parser.add_argument("--build-index", action="store_true", help="构建模板索引后退出")
    args = parser.parse_args()

    if args.build_index:
        from build_template_index import build_index
        from retrieval import build_features_from_index

        build_index()
        build_features_from_index()
        print(f"索引: {INDEX_PATH}")
        return

    app = CameraSketchToCadQuery()
    app.run(image_path=args.image)


if __name__ == "__main__":
    main()
    print("\n按回车键退出...")
    input()
