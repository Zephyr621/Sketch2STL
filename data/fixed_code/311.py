import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate with Rounded Corners ---
part_1_length = 0.7326 * 0.7326  # Scaled length
part_1_width = 0.436 * 0.7326  # Scaled width
part_1_height = 0.0174
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_1_length, 0.0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0.0, part_1_width)
    .close()
    .extrude(-part_1_height)
)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cut Feature ---
part_2_length = 0.5357 * 0.5357  # Scaled length
part_2_width = 0.5357 * 0.5357  # Scaled width
part_2_height = 0.2143
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(part_2_length, part_2_width
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_311.stl