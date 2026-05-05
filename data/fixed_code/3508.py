import cadquery as cq
from math import radians
# --- Part 1: Vertical Section ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.125)
    .lineTo(0.5, 0.125)
    .lineTo(0.5, 0.25)
    .lineTo(0.25, 0.25)
    .lineTo(0.25, 0.5)
    .lineTo(0.0, 0.5)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.125)
)
# --- Part 2: Rectangular Block ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.25 * 0.25, 0.125 * 0.25)
    .extrude(0.125)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3508.stl