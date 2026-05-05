import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75
part_1_width = 0.375 * 0.75
part_1_height = 0.0188
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# Holes in Part 1
hole_radius = 0.0062 * 0.75
hole1_x = 0.0312 * 0.75 - part_1_length/2
hole1_y = 0.1125 * 0.75 - part_1_width/2
hole2_x = 0.6281 * 0.75 - part_1_length/2
hole2_y = 0.1125 * 0.75 - part_1_width/2
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x, hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_654.stl