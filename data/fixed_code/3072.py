import cadquery as cq
from math import radians
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75
part_1_width = 0.4738 * 0.75
part_1_height = 0.0113
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0113, 0))
# --- Part 2: Flange ---
part_2_length = 0.7212 * 0.7212
part_2_width = 0.2784 * 0.7212
part_2_height = 0.0076
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0226, 0, 0.0226))
# ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3072.stl