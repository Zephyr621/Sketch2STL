import cadquery as cq
from math import *
# --- Part 1: Door Stopper ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3502 * 0.75, 0.0)
    .lineTo(0.3502 * 0.75, 0.5156 * 0.75)
    .threePointArc((0.1667 * 0.75, 0.5833 * 0.75), (0.1776 * 0.75, 0.7031 * 0.75))
    .lineTo(0.0829 * 0.75, 0.7031 * 0.75)
    .threePointArc((0.0572 * 0.75, 0.5833 * 0.75), (0.0, 0.5156 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1587)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1587))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2770.stl