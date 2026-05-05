import cadquery as cq
from math import radians
# --- Part 1: Base Rectangle ---
part_1_length = 0.75 * 0.75
part_1_width = 0.6875 * 0.75
part_1_height = 0.1875
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Vertical Extension ---
part_2_length = 0.7125 * 0.7125
part_2_width = 0.5625 * 0.7125
part_2_height = 0.0469
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0.0094 * 0.7125)
    .threePointArc((0.0134 * 0.7125, 0), (0.0094 * 0.7125, 0.0094 * 0.7125))
    .lineTo(0, 0.0094 * 0.7125)
    .close()
    .extrude(part_2_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3561.stl