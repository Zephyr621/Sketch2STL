import cadquery as cq
from math import radians
# --- Part 1: Base Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.1825
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Top Cube ---
part_2_length = 0.5625 * 0.5625  # Scaled length
part_2_width = 0.5625 * 0.5625   # Scaled width
part_2_height = 0.0312
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0937, 0.2813, 0.1825))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2414.stl