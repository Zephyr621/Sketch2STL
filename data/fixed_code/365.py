import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0313 * sketch_scale
# Scaled dimensions
arc1_start = (0.0 * sketch_scale, 0.0749 * sketch_scale)
arc1_mid = (0.0276 * sketch_scale, 0.0274 * sketch_scale)
arc1_end = (0.7059 * sketch_scale, 0.0749 * sketch_scale)
line1_end = (0.6726 * sketch_scale, 0.0 * sketch_scale)
arc2_start = (0.6726 * sketch_scale, 0.0 * sketch_scale)
arc2_mid = (0.7366 * sketch_scale, 0.0274 * sketch_scale)
arc2_end = (0.75 * sketch_scale, 0.0749 * sketch_scale)
line2_end = (0.75 * sketch_scale, 0.6726 * sketch_scale)
arc3_start = (0.75 * sketch_scale, 0.6726 * sketch_scale)
arc3_mid = (0.7366 * sketch_scale, 0.6043
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_365.stl