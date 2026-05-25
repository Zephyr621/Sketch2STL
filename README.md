# Sketch2STL

摄像头或本地图片中的手绘草图 → 匹配 `data/` 中的 CadQuery 模板 → 导出 STL；匹配失败时回退为基本体（立方体、球体等）。

## 环境

```bash
pip install -r requirements.txt
```

需要 Python 3.8+，Windows 上建议已安装 CadQuery（含 OCCT）。

## 首次使用：构建模板索引

```bash
python build_template_index.py
```

默认只索引 **有对应 STL** 的模板（约 260+ 个，速度快）。若要扫描全部 `fixed_code`：

```bash
python build_template_index.py --full
```

会生成：

- `data/template_index.json` — 模板语法校验、STL 关联
- `data/template_features.npz` — 轮廓特征（用于检索）

调试时可限制扫描数量：`python build_template_index.py --max 50`

## 运行

摄像头模式：

```bash
python camera_capture.py
```

本地图片（无需摄像头）：

```bash
python camera_capture.py --image path/to/sketch.jpg
```

构建索引并退出：

```bash
python camera_capture.py --build-index
```

## 输出

结果保存在 `output/`：

| 文件 | 说明 |
|------|------|
| `captured_raw.jpg` | 原始草图 |
| `processed_binary.jpg` | 二值化结果 |
| `contour_preview.jpg` | 轮廓叠加预览 |
| `matched_<id>.stl` | 模板匹配结果 |
| `cube_*.stl` 等 | 基本体回退结果 |

## 流程

1. 采集草图（摄像头或 `--image`）
2. 预处理与轮廓提取
3. 与 `data/all_stl_files` 中 STL 的投影视轮廓做 `matchShapes` 检索
4. 命中则复制或执行对应 `data/fixed_code/<id>.py`（匹配分数越小越好，默认 ≤ 1.5 即采用）
5. 未命中则按轮廓启发式生成基本体

若升级了轮廓匹配逻辑，建议重新构建特征：

```bash
python build_template_index.py
```

## 项目结构

```
camera_capture.py      # 主程序
build_template_index.py
config.py
template_sanitize.py   # 修复损坏的 CadQuery 模板
silhouette.py          # STL / 草图轮廓
retrieval.py           # 模板检索
template_runner.py     # 子进程执行模板
primitives.py          # 基本体回退
data/
  fixed_code/          # CadQuery 模板库
  all_stl_files/       # 参考 STL（用于轮廓索引）
```
