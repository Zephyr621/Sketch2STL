import cadquery as cq
from math import radians
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.74411 * 0.74411, 0.0)
    .lineTo(0.74411 * 0.74411, 0.1446 * 0.74411)
    .lineTo(0.2812 * 0.74411, 0.1446 * 0.74411)
    .lineTo(0.2812 * 0.74411, 0.2488 * 0.74411)
    .lineTo(0.0, 0.2488 * 0.74411)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.075)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0085, 0))
# --- Part 2: Cutout 1 ---
cut_radius = 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3510.stl