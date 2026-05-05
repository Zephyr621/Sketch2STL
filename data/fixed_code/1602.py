import cadquery as cq
from math import radians
# --- Part 1: Base ---
part_1_length = 0.5154 * 0.5154  # Scaled length
part_1_width = 0.5509 * 0.5154  # Scaled width
part_1_height = 0.3448
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0312, 0.3448, 0))
# --- Part 2: Vertical Extension ---
part_2_length = 0.2768 * 0.2768  # Scaled length
part_2_width = 0.1083 * 0.2768  # Scaled width
part_2_height = 0.0095
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1602.stl