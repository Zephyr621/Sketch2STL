import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * part_1_scale, 0.0)
    .lineTo(0.375 * part_1_scale, 0.25 * part_1_scale)
    .lineTo(0.1875 * part_1_scale, 0.25 * part_1_scale)
    .lineTo(0.1875 * part_1_scale, 0.5 * part_1_scale)
    .lineTo(0.0, 0.5 * part_1_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.25 * part_1_scale)
)
# Coordinate System Transformation for Part 1
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 =
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1936.stl