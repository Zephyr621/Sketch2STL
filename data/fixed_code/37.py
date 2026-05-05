import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.3261 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.229
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.229, 0))
# --- Part 2: Rectangular Block (Cutout) ---
part_2_length = 0.0158 * 0.7421
part_2_width = 0.7421 * 0.7421
part_2_height = 0.0341
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_37.stl