import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Teardrop-shaped base ---
part_1_scale = 0.6926
part_1_depth = 0.0416
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0031 * part_1_scale)
    .lineTo(0.0583 * part_1_scale, 0.0)
    .lineTo(0.6328 * part_1_scale, 0.0)
    .lineTo(0.6926 * part_1_scale, 0.0031 * part_1_scale)
    .lineTo(0.6926 * part_1_scale, 0.1143 * part_1_scale)
    .lineTo(0.0583 * part_1_scale, 0.1143 * part_1_scale)
    .close()
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2015.stl