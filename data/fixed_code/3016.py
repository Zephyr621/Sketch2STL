import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.0117
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0117, 0))
# --- Part 2: Cube ---
part_2_size = 0.0352 * 0.3625  # Scaled size
part_2_height = 0.0117
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3016.stl