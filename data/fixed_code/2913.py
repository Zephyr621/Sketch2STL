import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0065 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1346 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.1346 * sketch_scale)
    .threePointArc((0.3751 * sketch_scale, 0.0), (0.75 * sketch_scale, 0.1346 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2885 * sketch_scale)
    .threePointArc((0.3751 * sketch_scale, 0.1421 * sketch_scale), (0.375 * sketch_scale, 0.2885 * sketch_scale))
    .lineTo(0.375 * sketch_scale, 0.1421 * sketch_scale)
    .threePointArc((0.3751 * sketch_scale, 0.2118 * sketch_scale), (0.375 * sketch_scale, 0.2885 * sketch_scale))
    .lineTo(0.1587 * sketch_scale, 0.2885 * sketch_scale)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2913.stl