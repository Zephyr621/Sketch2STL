import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.125)
    .lineTo(0.5625, 0.125)
    .lineTo(0.375, 0.375)
    .lineTo(0.1875, 0.375)
    .lineTo(0.1875, 0.125)
    .lineTo(0.0, 0.125)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1562 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1562 * 0.75, 0))
# --- Part 2: Cyl
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1228.stl