import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate ---
part_1_length = 0.45 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0051
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cube ---
part_2_size = 0.45 * 0.45
part_2_height = 0.0104
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2890.stl