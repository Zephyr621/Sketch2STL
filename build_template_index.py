#!/usr/bin/env python3
"""扫描模板、校验语法、关联 STL，并生成检索索引。

用法:
  python build_template_index.py
  python build_template_index.py --max 500   # 仅扫描前 500 个（调试）
"""
import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from config import DATA_DIR, FIXED_CODE_DIR, INDEX_PATH, PROJECT_ROOT, STL_DIR
from retrieval import build_features_from_index
from silhouette import stl_to_contour
from template_sanitize import check_syntax, sanitize_template_code, template_id_from_path


def find_stl_for_id(template_id: str) -> Optional[Path]:
    candidates = [
        STL_DIR / f"output_{template_id}.stl",
        DATA_DIR / "all_stl_files" / f"output_{template_id}.stl",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def _collect_template_files(stl_only: bool, max_files: Optional[int]) -> List[Path]:
    if stl_only:
        files = []
        for stl in sorted(STL_DIR.glob("output_*.stl")):
            tid = stl.stem.replace("output_", "", 1)
            code = FIXED_CODE_DIR / f"{tid}.py"
            if code.exists():
                files.append(code)
        print(f"STL 关联模式: {len(files)} 个模板（有对应 STL）")
    else:
        files = sorted(
            p for p in FIXED_CODE_DIR.glob("*.py") if not p.name.startswith("exec_")
        )
        print(f"全量扫描模式: {len(files)} 个模板文件")
    if max_files:
        files = files[:max_files]
    return files


def build_index(max_files: Optional[int] = None, stl_only: bool = True) -> dict:
    templates = []
    files = _collect_template_files(stl_only=stl_only, max_files=max_files)

    for path in files:
        template_id = template_id_from_path(path)
        raw = path.read_text(encoding="utf-8", errors="ignore")
        cleaned = sanitize_template_code(raw, template_id)
        ok, err = check_syntax(cleaned)

        stl_path = find_stl_for_id(template_id)
        has_stl = stl_path is not None
        has_silhouette = False
        if has_stl:
            has_silhouette = stl_to_contour(stl_path) is not None

        rel_code = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        rel_stl = None
        if stl_path:
            rel_stl = str(stl_path.relative_to(PROJECT_ROOT)).replace("\\", "/")

        templates.append(
            {
                "id": template_id,
                "code_path": rel_code,
                "syntax_ok": ok,
                "syntax_error": err,
                "stl_path": rel_stl,
                "has_stl": has_stl,
                "has_silhouette": has_silhouette,
            }
        )

    syntax_ok = sum(1 for t in templates if t["syntax_ok"])
    with_sil = sum(1 for t in templates if t["has_silhouette"])

    index = {
        "version": 1,
        "stats": {
            "total": len(templates),
            "syntax_ok": syntax_ok,
            "with_silhouette": with_sil,
        },
        "templates": templates,
    }
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"索引已写入: {INDEX_PATH}")
    print(f"  总计: {len(templates)}, 语法通过: {syntax_ok}, 可检索(有轮廓): {with_sil}")
    return index


def main():
    parser = argparse.ArgumentParser(description="构建 Sketch2STL 模板索引")
    parser.add_argument("--max", type=int, default=None, help="最多扫描文件数")
    parser.add_argument(
        "--full",
        action="store_true",
        help="扫描全部 fixed_code（默认仅索引有 STL 的模板）",
    )
    parser.add_argument("--skip-features", action="store_true", help="不生成轮廓特征文件")
    args = parser.parse_args()

    build_index(max_files=args.max, stl_only=not args.full)
    if not args.skip_features:
        n = build_features_from_index()
        print(f"轮廓特征已写入, 可检索模板数: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
