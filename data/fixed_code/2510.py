import cadquery as cq
from math import *
# --- Part 1: Cube with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.0282 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.7125 * sketch_scale)
    .lineTo(0.0361 * sketch_scale, 0.7125 * sketch_scale)
    .lineTo(0.0361 * sketch_scale, 0.3586 * sketch_scale)
    .lineTo(0.5357 * sketch_scale, 0.3586 * sketch_scale)
    .lineTo(0.5357 * sketch_scale, 0.2143 * sketch_scale)
    .lineTo(0.3107 * sketch_scale, 0.2143 * sketch_scale)
    .lineTo(0.3107 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.7125 * sketch_scale)
    .lineTo(0.4286 * sketch_scale, 0.7125 * sketch_scale)
    .lineTo(0.4286 * sketch_scale, 0.7125 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2510.stl