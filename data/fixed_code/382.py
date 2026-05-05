import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Curved Edges ---
sketch_scale = 0.75
extrude_depth = 0.3333
# Scaled dimensions
line_1_start_x = 0.0 * sketch_scale
line_1_end_x = 0.1667 * sketch_scale
line_1_mid_y = 0.0833 * sketch_scale
arc_1_mid_y = 0.4167 * sketch_scale
arc_2_mid_y = 0.5333 * sketch_scale
arc_3_mid_y = 0.5717 * sketch_scale
arc_4_mid_y = 0.5833 * sketch_scale
line_2_end_x = 0.375 * sketch_scale
line_2_end_y = 0.25 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(line_1_start_x, line_1_end_y)
    .lineTo(line_1_end_x, line_1_end_y)
    .threePointArc((arc_1_mid_y, arc_2_mid_y), (line_2_end_x, line_2_end_y))
    .lineTo(line_1_start
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_382.stl