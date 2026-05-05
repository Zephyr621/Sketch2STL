import cadquery as cq
from math import *
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2494, 0.0)
    .lineTo(0.2494, 0.0188)
    .lineTo(0.2533, 0.0188)
    .lineTo(0.2533, 0.7498)
    .lineTo(0.2494, 0.7498)
    .lineTo(0.2494, 0.75)
    .lineTo(0.0, 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0075 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0075, 0))
# --- Assembly ---
assembly = part_1
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2538.stl