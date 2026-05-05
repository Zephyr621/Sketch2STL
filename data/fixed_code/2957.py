import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.3
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0015 * sketch_scale, 0.0015 * sketch_scale)
    .threePointArc((0.0117 * sketch_scale, 0), (0.0015 * sketch_scale, 0.0295 * sketch_scale))
    .lineTo(0.7 * sketch_scale, 0.0295 * sketch_scale)
    .threePointArc((0.747 * sketch_scale, 0.0117 * sketch_scale), (0.75 * sketch_scale, 0.0015 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1266 * sketch_scale)
    .threePointArc((0.747 * sketch_scale, 0.2407 * sketch_scale), (0.75 * sketch_scale, 0.2479 * sketch_scale))
    .lineTo(0.7 * sketch_scale, 0.2479 * sketch_scale)
    .threePointArc((0.747 * sketch_scale, 0.2407 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2957.stl