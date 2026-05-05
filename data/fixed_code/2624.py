import cadquery as cq
from math import radians
# --- Part 1: Curved Shape ---
part_1_scale = 0.75
part_1_height = 0.0417 * part_1_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.09)
    .lineTo(0.09, 0.09)
    .threePointArc((0.375 * part_1_scale, 0.65 * part_1_scale), (0.5625 * part_1_scale, 0.09))
    .lineTo(0.75 * part_1_scale, 0.09)
    .lineTo(0.75 * part_1_scale, 0.7159 * part_1_scale)
    .lineTo(0.5625 * part_1_scale, 0.7159 * part_1_scale)
    .threePointArc((0.375 * part_1_scale, 0.64 * part_1_scale), (0.0, 0.7159 * part_1_scale))
    .lineTo(0.0, 0.09)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2624.stl