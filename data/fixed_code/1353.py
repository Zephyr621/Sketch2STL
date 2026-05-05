import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Curved Base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0144 * 0.75)
    .threePointArc((0.375 * 0.75, 0.1786 * 0.75), (0.75 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0792 * 0.75)
    .lineTo(0.6593 * 0.75, 0.0792 * 0.75)
    .threePointArc((0.375 * 0.75, 0.3471 * 0.75), (0.0, 0.0792 * 0.75))
    .close()
    .extrude(0.075)
)
# --- Part 2: Cutout 1 ---
cutout_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0144 * 0.375)
    .lineTo(0.1579 * 0.375, 0.0144 * 0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1353.stl