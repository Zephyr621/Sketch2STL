import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.0841 * 0.1402  # Scaled length
part_1_width = 0.1402 * 0.1402  # Scaled width
part_1_height = 0.1227
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.6659, 0.321, 0))
# --- Part 2: L-Shaped Cutout ---
part_2_length = 0.0817 * 0.0833  # Scaled length
part_2_width = 0.0833 * 0.0833  # Scaled width
part_2_height = 0.0767
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1262.stl