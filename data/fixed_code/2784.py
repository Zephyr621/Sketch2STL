import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate ---
sketch_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.1309 * sketch_scale)
    .threePointArc((0.0053 * sketch_scale, 0.0053 * sketch_scale), (0.1309 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.7292 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.0053 * sketch_scale), (0.75 * sketch_scale, 0.1309 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2143 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.3293 * sketch_scale), (0.7292 * sketch_scale, 0.3314 * sketch_scale))
    .lineTo(0.1309 * sketch_scale, 0.3314 * sketch_scale)
    .threePointArc((0.0053 * sketch_scale, 0.3293 * sketch_scale),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2784.stl