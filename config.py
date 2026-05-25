from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
FIXED_CODE_DIR = DATA_DIR / "fixed_code"
STL_DIR = DATA_DIR / "all_stl_files"
INDEX_PATH = DATA_DIR / "template_index.json"
FEATURES_PATH = DATA_DIR / "template_features.npz"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 轮廓检索（cv2.matchShapes，越小越相似；典型好匹配约 0.3~1.5）
RETRIEVAL_MAX_SCORE = 1.5
# Top1 与 Top2 分数差至少为此值时才认为“有明确最佳”（可选加强）
RETRIEVAL_MIN_GAP = 0.08
RETRIEVAL_TOP_K = 3
