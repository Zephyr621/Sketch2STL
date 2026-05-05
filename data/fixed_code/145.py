import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Bracket ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.375 * sketch_scale
height = 0.125
# Hole parameters (scaled)
hole1_center = (0.0625 * sketch_scale, 0.2812 * sketch_scale)
hole2_center = (0.5625 * sketch_scale, 0.1875 * sketch_scale)
hole3_center = (0.75 * sketch_scale, 0.2812 * sketch_scale)
hole_radius = 0.0313 * sketch_scale
# Create the base shape with arcs
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + (0.5625 - 0.0625)/2, 0.0625), (length, width))
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# Cut the holes
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .hole(2 * hole_radius)
)
part_1 = (
    part_1.faces(">Z")
    .workplane()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_145.stl