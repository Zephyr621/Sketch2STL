import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_length = 0.6 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.15
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.15, 0))
# --- Part 2: Cutout ---
part_2_length = 0.3 * 0.3
part_2_width = 0.1875 * 0.3
part_2_height = 0.15
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1305.stl