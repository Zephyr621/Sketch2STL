import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Beam ---
sketch_scale = 0.75
extrude_depth = 0.0156 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0062 * sketch_scale)
    .lineTo(0.0703 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0469 * sketch_scale), (0.6731 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0547 * sketch_scale)
    .lineTo(0.6731 * sketch_scale, 0.0938 * sketch_scale)
    .lineTo(0.7187 * sketch_scale, 0.0938 * sketch_scale)
    .threePointArc((0.3723 * sketch_scale, 0.0469 * sketch_scale), (0.5341 * sketch_scale, 0.0938 * sketch_scale))
    .lineTo(0.4286 * sketch_scale, 0.0938 * sketch_scale)
    .lineTo(0.1793 * sketch_scale, 0.0938 * sketch_scale)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1885.stl