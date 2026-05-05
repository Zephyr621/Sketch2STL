import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.6 * sketch_scale
height = 0.3
# Create the base shape
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.15 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.075 * sketch_scale), (0.15 * sketch_scale, 0.45 * sketch_scale))
    .lineTo(0.0, 0.45 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.6 * sketch_scale), (0.0, 0.6 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(height)
)
# Create the hole
hole_radius = 0.0375 * sketch_scale
part_1 = part_1.faces(">Z").workplane().center(0.3 * sketch_scale - length/2, 0.3 * sketch_scale - width/2).circle(hole_radius).cutThruAll()
# --- Part 2: Cutout ---
sketch_scale_part2 =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1983.stl