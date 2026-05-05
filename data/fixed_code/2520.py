import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_length = 0.300 * 0.300  # Scaled length
part_1_width = 0.300 * 0.300  # Scaled width
part_1_height = 0.15
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cutout ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.15 * 0.75  # Scaled width
part_2_height = 0.0059
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2520.stl