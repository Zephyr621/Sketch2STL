import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2395 * 0.75)
    .lineTo(0.5208 * 0.75, 0.2395 * 0.75)
    .lineTo(0.5208 * 0.75, 0.4737 * 0.75)
    .lineTo(0.1178 * 0.75, 0.4737 * 0.75)
    .lineTo(0.1178 * 0.75, 0.2395 * 0.75)
    .lineTo(0.0, 0.2395 * 0.75)
    .close()
    .extrude(-0.3289)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Holes ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2747.stl