import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Box with Rounded Corners ---
sketch_scale = 0.5357
extrude_depth = 0.75
# Scaled dimensions
arc_1_start = (0.1667 * sketch_scale, 0)
arc_1_mid = (0.2571 * sketch_scale, 0.0)
arc_1_end = (0.5357 * sketch_scale, 0.0893 * sketch_scale)
arc2_start = (0.5357 * sketch_scale, 0.0893 * sketch_scale)
arc2_mid = (0.2571 * sketch_scale, 0.2143 * sketch_scale)
arc2_end = (0.1667 * sketch_scale, 0.2143 * sketch_scale)
line_1_start = (0.1667 * sketch_scale, 0.2143 * sketch_scale)
line_1_end = (0.1667 * sketch_scale, 0.0893 * sketch_scale)
line_2_start = (0.1667 * sketch_scale, 0.0893 * sketch_scale)
line_2_end = (0.1667 * sketch_scale, 0.2143 * sketch_scale)
circle_1_center = (0.1667 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2564.stl