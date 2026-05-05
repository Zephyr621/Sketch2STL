import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.5
# Scaled dimensions
arc_1_start = (0.1749 * sketch_scale, 0.0)
arc_1_mid = (0.375 * sketch_scale, 0.0303 * sketch_scale)
arc_1_end = (0.5 * sketch_scale, 0.0)
arc_2_start = (0.5 * sketch_scale, 0.0)
arc_2_mid = (0.75 * sketch_scale, 0.625 * sketch_scale)
arc_2_end = (0.5 * sketch_scale, 0.625 * sketch_scale)
arc_3_start = (0.5 * sketch_scale, 0.625 * sketch_scale)
arc_3_mid = (0.375 * sketch_scale, 0.4125 * sketch_scale)
arc_3_end = (0.1749 * sketch_scale, 0.625 * sketch_scale)
arc_4_start = (0.1749 * sketch_scale, 0.625 * sketch_scale)
arc_4_mid = (0.0 * sketch_scale, 0.4125 * sketch_scale)
arc_4_end = (0.1749 * sketch_scale, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2713.stl