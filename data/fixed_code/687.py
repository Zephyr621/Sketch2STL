import cadquery as cq
from math import radians
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .close()
    .extrude(-0.4687 * 0.75)
)
# --- Part 2: Rectangular protrusion ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1875 * 0.75)
    .lineTo(0.0, 0.1875 * 0.75)
    .close()
    .extrude(-0.3125 * 0.75)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0.2812, 0.4687))
# --- Assembly ---
assembly = part_1.union(part_2)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_687.stl