import cadquery as cq
from math import radians
# --- Part 1: Flat Plate ---
part_1_scale = 0.75
part_1_depth = 0.0156
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0937 * part_1_scale, 0.0)
    .threePointArc((0.375 * part_1_scale, 0.0937 * part_1_scale), (0.6563 * part_1_scale, 0.0))
    .lineTo(0.75 * part_1_scale, 0.0)
    .lineTo(0.75 * part_1_scale, 0.5625 * part_1_scale)
    .lineTo(0.6977 * part_1_scale, 0.5625 * part_1_scale)
    .lineTo(0.375 * part_1_scale, 0.2812 * part_1_scale)
    .lineTo(0.0, 0.5625 * part_1_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2804.stl