import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.18 * 0.75  # Scaled width
part_1_height = 0.18
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.18, 0))
# --- Part 2: Cylinder with Hole ---
outer_radius = 0.0525 * 0.11  # Scaled outer radius
inner_radius = 0.0234 * 0.11  # Scaled inner radius
hole_center_x = 0.0525 * 0.11  # Scaled hole center x
hole_center_y = 0.0525 * 0.11  # Scaled hole center y
hole_radius = 0.0162 * 0.11  # Scaled hole radius
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2678.stl