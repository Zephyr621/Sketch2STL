import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5 * 0.75)
    .lineTo(0.375 * 0.75, 0.5 * 0.75)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.125 * 0.75, 0.25 * 0.75)
    .lineTo(0.125 * 0.75, 0.625 * 0.75)
    .lineTo(0.0, 0.625 * 0.75)
    .lineTo(0.0, 0.5 * 0.75)
    .close()
    .extrude(0.0562 * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_106.stl