import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.7555 * 0.7555  # Scaled length
part_1_width = 0.2518 * 0.7555  # Scaled width
part_1_height = 0.1259
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0075, 0.0075, 0))
# --- Part 2: Cylindrical Holes ---
hole_radius = 0.0054 * 0.7031  # Scaled radius
hole_depth = 0.7031
hole_centers = [
    (0.0054 * 0.7031, 0.0054 * 0.7031),
    (0.0054 * 0.7031, 0.6201 * 0.7031),
    (0.6201 * 0.7031, 0.0054 * 0.7031),
    (0.6201 * 0.7031, 0.6201 * 0.7031)
]
# Create holes by cutting cylinders
for center_x, center_y in hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3369.stl