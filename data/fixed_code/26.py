import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0288 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0477 * sketch_scale)
    .lineTo(0.1671 * sketch_scale, 0.0169 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.0074 * sketch_scale), (0.4773 * sketch_scale, 0.0064 * sketch_scale))
    .lineTo(0.7102 * sketch_scale, 0.0169 * sketch_scale)
    .threePointArc((0.6836 * sketch_scale, 0.0), (0.6609 * sketch_scale, 0.0065 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.3376 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0341 * sketch_scale)
    .lineTo(0.4773 * sketch_scale, 0.0341 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.1137 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_26.stl