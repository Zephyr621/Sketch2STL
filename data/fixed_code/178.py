import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Corners ---
part_1_length = 0.6 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.015
corner_radius = 0.05 * 0.75
hole_radius = 0.0058 * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .lineTo(0, part_1_width - corner_radius)
    .threePointArc((corner_radius, 0), (part_1_length - corner_radius, part_1_width))
    .lineTo(part_1_length, part_1_width)
    .threePointArc((part_1_length - corner_radius, part_1_width), (part_1_length - corner_radius, part_1_width + corner_radius))
    .lineTo(part_1_length, part_1_width + corner_radius)
    .threePointArc((part_1_length - corner_radius, part_1_width + corner_radius), (part_1_length - corner_radius, part_1_width + corner_radius))
    .lineTo(corner_radius, part_1_width)
    .threePointArc((0, part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_178.stl