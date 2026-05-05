import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.25 * 0.75  # Scaled width
part_1_height = 0.05
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Part 2: Cylindrical Cutout ---
part_2_radius = 0.0937 * 0.1875  # Scaled radius
part_2_depth = 0.125
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0469, 0.0469)  # Move to the origin
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0312, 0.0312, part_1_height))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1254.stl