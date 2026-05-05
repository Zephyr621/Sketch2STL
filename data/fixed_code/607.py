import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0857 * sketch_scale)
    .threePointArc((0.0366 * sketch_scale, 0.1279 * sketch_scale), (0.1714 * sketch_scale, 0.1168 * sketch_scale))
    .lineTo(0.6284 * sketch_scale, 0.1038 * sketch_scale)
    .threePointArc((0.75 * sketch_scale, 0.1279 * sketch_scale), (0.5357 * sketch_scale, 0.0857 * sketch_scale))
    .lineTo(0.6736 * sketch_scale, 0.0719 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.1349 * sketch_scale), (0.5357 * sketch_scale, 0.0 * sketch_scale))
    .threePointArc((0.6736 * sketch_scale, 0.1451 * sketch_scale), (0.6736 * sketch_scale, 0.2344 * sketch_scale))
    .lineTo(0.0429 * sketch_scale, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_607.stl