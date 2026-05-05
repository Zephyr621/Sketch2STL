import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0268 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0536 * sketch_scale)
    .threePointArc((0.0268 * sketch_scale, 0.0268 * sketch_scale), (0.0536 * sketch_scale, 0.0))
    .lineTo(0.6964 * sketch_scale, 0.0)
    .threePointArc((0.7339 * sketch_scale, 0.0268 * sketch_scale), (0.75 * sketch_scale, 0.0536 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.5357 * sketch_scale)
    .threePointArc((0.7339 * sketch_scale, 0.4286 * sketch_scale), (0.6964 * sketch_scale, 0.5357 * sketch_scale))
    .lineTo(0.0536 * sketch_scale, 0.5357 * sketch_scale)
    .threePointArc((0.0268 * sketch_scale, 0.4286 * sketch_scale), (0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2555.stl