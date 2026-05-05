import cadquery as cq
from math import radians
# --- Part 1: Rectangular Plate with Curved Edges ---
sketch_scale = 0.75
extrude_depth = 0.0188
# Scaled dimensions
width = 0.5 * sketch_scale
length = 0.75 * sketch_scale
arc_mid_x = 0.75 * sketch_scale
arc_mid_y = 0.25 * sketch_scale
arc_end_x1 = 0.12 * sketch_scale
arc_end_x2 = 0.375 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_start_y)
    .threePointArc((arc_mid_x, arc_mid_y), (arc_end_x1, arc_end_y))
    .lineTo(line_end_x1, line_end_y)
    .threePointArc((arc_mid_x, arc_mid_y - arc_mid_y), (0, arc_start_y))
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1670.stl