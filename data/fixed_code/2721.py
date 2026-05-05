import cadquery as cq
from math import *
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.4167)
    .lineTo(0.6167, 0.4167)
    .lineTo(0.6167, 0.2165)
    .lineTo(0.3125, 0.2165)
    .lineTo(0.3125, 0.4167)
    .lineTo(0.0, 0.4167)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3333)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3333, 0))
# --- Part 2: Cutout ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.15 * 0.4225, 0.4225 * 0.4225)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2721.stl