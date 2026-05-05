import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1667 * 0.75)
    .lineTo(0.6667 * 0.75, 0.1667 * 0.75)
    .lineTo(0.6667 * 0.75, 0.2259 * 0.75)
    .lineTo(0.1042 * 0.75, 0.2259 * 0.75)
    .lineTo(0.1042 * 0.75, 0.1667 * 0.75)
    .lineTo(0.0, 0.1667 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1355)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1485.stl