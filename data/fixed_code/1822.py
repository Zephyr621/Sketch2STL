import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0625
# Scaled dimensions
arc1_start = (0.1749 * sketch_scale, 0.0)
arc1_mid = (0.375 * sketch_scale, 0.0303 * sketch_scale)
arc1_end = (0.5751 * sketch_scale, 0.0)
arc2_start = (0.5751 * sketch_scale, 0.0)
arc2_mid = (0.75 * sketch_scale, 0.375 * sketch_scale)
arc2_end = (0.5751 * sketch_scale, 0.375 * sketch_scale)
arc3_start = (0.5751 * sketch_scale, 0.375 * sketch_scale)
arc3_mid = (0.375 * sketch_scale, 0.375 * sketch_scale)
arc3_end = (0.1749 * sketch_scale, 0.375 * sketch_scale)
circle1_center = (0.1349 * sketch_scale, 0.1875 * sketch_scale)
circle1_radius = 0.0656 * sketch_scale
circle2_center = (0.6151 * sketch_scale, 0.18
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1822.stl