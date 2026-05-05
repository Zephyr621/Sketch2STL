import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0033
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1167 * sketch_scale, 0.0245 * sketch_scale)
    .threePointArc((0.0, 0.1579 * sketch_scale), (0.1167 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .threePointArc((0.7333 * sketch_scale, 0.1442 * sketch_scale), (0.75 * sketch_scale, 0.5357 * sketch_scale))
    .lineTo(0.6136 * sketch_scale, 0.5708 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.4286 * sketch_scale), (0.6136 * sketch_scale, 0.5893 * sketch_scale))
    .lineTo(0.1167 * sketch_scale, 0.5893 * sketch_scale)
    .threePointArc((0.0144 * sketch_scale, 0.2983 * sketch_scale), (0.1167 * sketch_scale, 0.5708 * sketch_scale))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2185.stl