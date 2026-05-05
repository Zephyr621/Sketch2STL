import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.5 * 0.5  # Scaled length
part_1_width = 0.125 * 0.5  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cut Feature ---
part_2_length = 0.5 * 0.5  # Scaled length
part_2_width = 0.375 * 0.5  # Scaled width
part_2_height = 0.25
cut_feature = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2972.stl