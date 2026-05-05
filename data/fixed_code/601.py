import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.15 * 0.75  # Scaled width
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Part 2: Holes ---
hole_radius = 0.0058 * 0.7159  # Scaled radius
hole_depth = 0.03
hole1_x = 0.0238 * 0.7159
hole1_y = 0.0238 * 0.7159
hole2_x = 0.6435 * 0.7159
hole2_y = 0.0238 * 0.7159
part_2 = (
    cq.Workplane("XY")
    .moveTo(hole1_x, hole1_y)
    .circle(hole_radius)
    .moveTo(hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_601.stl