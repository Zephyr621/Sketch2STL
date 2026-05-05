import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3971 * 0.75  # Scaled width
part_1_height = 0.0964
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0833 * 0.6635  # Scaled radius
part_2_depth = 0.1276
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0465, 0.0379, 0.0586))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_86.stl