import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.03
# Scaled dimensions
arc_radius1 = 0.0429 * sketch_scale
arc_radius2 = 0.0415 * sketch_scale
arc_radius3 = 0.0607 * sketch_scale
arc_radius4 = 0.0457 * sketch_scale
line_length = 0.7288 * sketch_scale
total_height = 0.0863 * 2  # Total height (towards + opposite)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius1)
    .threePointArc((arc_radius1, 0), (0.0078 * sketch_scale, 0.0078 * sketch_scale))
    .lineTo(line_length, 0)
    .threePointArc((total_height, arc_radius1), (0.0078 * sketch_scale, 0.5759 * sketch_scale))
    .lineTo(arc_radius2, 0.5759 * sketch_scale)
    .threePointArc((arc_radius2, total_height
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2184.stl