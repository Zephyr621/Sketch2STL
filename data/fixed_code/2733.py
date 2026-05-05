import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0625
# Scaled dimensions
arc_radius = 0.0562 * sketch_scale
line_length = 0.6938 * sketch_scale
total_length = 0.75 * sketch_scale
width = 0.2125 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.0072 * sketch_scale, 0.0072 * sketch_scale))
    .lineTo(line_length, 0)
    .threePointArc((total_length, arc_radius), (0.7188 * sketch_scale, 0.0072 * sketch_scale))
    .lineTo(total_length, width - arc_radius)
    .threePointArc((line_length, width), (0.0072 * sketch_scale, width - arc_radius))
    .lineTo(0, width - arc_radius)
    .close()
    .extrude(extrude_depth)
)
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2733.stl