"""基于轮廓的模板检索。"""
import json
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

from config import (
    FEATURES_PATH,
    INDEX_PATH,
    RETRIEVAL_MAX_SCORE,
    RETRIEVAL_MIN_GAP,
    RETRIEVAL_TOP_K,
    STL_DIR,
)
from silhouette import binary_to_main_contour, contour_match_score, stl_to_contour


class TemplateRetriever:
    def __init__(
        self,
        index_path: Optional[Path] = None,
        features_path: Optional[Path] = None,
    ):
        self.index_path = index_path or INDEX_PATH
        self.features_path = features_path or FEATURES_PATH
        self.entries: List[Dict] = []
        self.contours: List[np.ndarray] = []
        self._loaded = False

    @property
    def available(self) -> bool:
        return self.index_path.exists()

    def load(self) -> int:
        if not self.index_path.exists():
            return 0
        if not self.features_path.exists():
            build_features_from_index(self.index_path)

        if not self.features_path.exists():
            return 0

        with open(self.index_path, encoding="utf-8") as f:
            data = json.load(f)
        self.entries = [e for e in data.get("templates", []) if e.get("has_silhouette")]

        archive = np.load(self.features_path, allow_pickle=True)
        ids = list(archive["ids"])
        contours = list(archive["contours"])

        id_to_contour = dict(zip(ids, contours))
        self.contours = []
        filtered = []
        for entry in self.entries:
            tid = entry["id"]
            if tid in id_to_contour:
                filtered.append(entry)
                self.contours.append(id_to_contour[tid])
        self.entries = filtered
        self._loaded = True
        return len(self.entries)

    def search(self, binary_image, top_k: Optional[int] = None) -> List[Dict]:
        if not self._loaded:
            self.load()
        if not self.entries:
            return []

        top_k = top_k or RETRIEVAL_TOP_K
        query = binary_to_main_contour(binary_image)
        if query is None:
            return []

        scored = []
        for entry, template_contour in zip(self.entries, self.contours):
            score = contour_match_score(query, template_contour)
            scored.append({**entry, "score": score})

        scored.sort(key=lambda x: x["score"])
        return scored[:top_k]

    def should_accept_match(self, matches: List[Dict]) -> bool:
        """判断是否采用模板检索结果（绝对阈值 + 相对 Top1/Top2 差距）。"""
        if not matches:
            return False
        top1 = matches[0]["score"]
        if top1 <= RETRIEVAL_MAX_SCORE:
            return True
        if len(matches) >= 2:
            gap = matches[1]["score"] - top1
            if gap >= RETRIEVAL_MIN_GAP and top1 <= RETRIEVAL_MAX_SCORE * 1.5:
                return True
        return False

    def best_match(self, binary_image) -> Optional[Dict]:
        results = self.search(binary_image, top_k=1)
        if not results:
            return None
        if not self.should_accept_match(results):
            return None
        return results[0]


def build_features_from_index(index_path: Optional[Path] = None) -> int:
    """根据 template_index.json 预计算轮廓特征。"""
    index_path = index_path or INDEX_PATH
    if not index_path.exists():
        return 0

    with open(index_path, encoding="utf-8") as f:
        data = json.load(f)

    ids = []
    contours = []
    for entry in data.get("templates", []):
        if not entry.get("has_silhouette"):
            continue
        stl_rel = entry.get("stl_path")
        if not stl_rel:
            continue
        stl_path = Path(__file__).parent / stl_rel
        if not stl_path.exists():
            stl_path = STL_DIR / f"output_{entry['id']}.stl"
        if not stl_path.exists():
            continue
        contour = stl_to_contour(stl_path)
        if contour is None:
            continue
        ids.append(entry["id"])
        contours.append(contour)

    if not ids:
        return 0

    np.savez(FEATURES_PATH, ids=np.array(ids, dtype=object), contours=np.array(contours, dtype=object))
    return len(ids)
