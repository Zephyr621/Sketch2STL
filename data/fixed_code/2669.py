import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.15
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.1875 * sketch_scale)
    .threePointArc((0.0105 * sketch_scale, 0.0105 * sketch_scale), (0.1875 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.5625 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7292 * sketch_scale, 0.0105 * sketch_scale), (0.75 * sketch_scale, 0.1875 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.375 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, 0.375 * sketch_scale)
    .threePointArc((0.7292 * sketch_scale, 0.3983 * sketch_scale), (0.5625 * sketch_scale, 0.1875 * sketch_scale))
    .lineTo(0.18
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2669.stl