import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Curved Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.25 * sketch_scale
height = 0.375
# Scaled values
arc_radius = 0.125 * sketch_scale
line_length = 0.5 * sketch_scale
total_length = 0.75 * sketch_scale
# Create the base rectangle
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.125 * sketch_scale, 0.125 * sketch_scale))
    .lineTo(length - arc_radius, 0)
    .threePointArc((length, arc_radius), (length - 0.625 * sketch_scale, 0.125 * sketch_scale))
    .lineTo(length, width - arc_radius)
    .threePointArc((length - arc_radius, width), (length - 0.625 * sketch_scale, width - 0.125 * sketch_scale))
    .lineTo(arc_radius, width)
    .threePointArc((0, width - arc_radius), (0.125 * sketch_scale, width - 0.125 * sketch_scale))
    .close()
    .extrude(height)
)
# Create the hole
hole_center
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3284.stl