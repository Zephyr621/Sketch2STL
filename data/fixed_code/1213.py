import cadquery as cq
from math import radians
# --- Part 1: Rectangular Base ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0469 * 0.5934  # Scaled radius
cylinder_height = 0.125
# Create the first cylinder
cylinder1 = (
    cq.Workplane("XY")
    .moveTo(0.0238 * 0.5934, 0.0068 * 0.5934)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)
# Create the second cylinder
cylinder2 = (
    cq.Workplane("XY")
    .moveTo(0.4732 * 0.5934, 0.0068 * 0.5934)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)
# Combine
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1213.stl