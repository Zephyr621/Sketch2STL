import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0375
# Scaled dimensions
arc_start_x = 0.0 * sketch_scale
arc_mid_y = 0.0 * sketch_scale
arc_end_x = 0.0938 * sketch_scale
arc_mid_y2 = 0.0 * sketch_scale
line1_end_x = 0.6562 * sketch_scale
line2_end_x = 0.6562 * sketch_scale
line3_end_x = 0.75 * sketch_scale
arc4_mid_y = 0.0577 * sketch_scale
arc4_end_y = 0.25 * sketch_scale
circle_center_x1 = 0.0938 * sketch_scale
circle_center_x2 = 0.6487 * sketch_scale
circle_center_y = 0.375 * sketch_scale
circle_radius = 0.0844 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(arc_start_x, arc_start_y)
    .lineTo(line1_end_x, line1_end_y)
    .threePointArc((arc_mid_x, arc_mid_y), (arc_end_x, arc_start_y))
    .lineTo(line2_end
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_838.stl