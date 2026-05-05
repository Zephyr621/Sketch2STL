import cadquery as cq
from math import *
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0937, 0.0)
    .lineTo(0.0937, 0.1875)
    .lineTo(0.6563, 0.1875)
    .lineTo(0.6563, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.375)
    .lineTo(0.5625, 0.375)
    .lineTo(0.5625, 0.1875)
    .lineTo(0.1875, 0.1875)
    .lineTo(0.1875, 0.375)
    .lineTo(0.0, 0.375)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0937 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_465.stl