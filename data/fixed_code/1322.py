import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0337 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0825 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.3409 * sketch_scale), (0.5769 * sketch_scale, 0.0))
    .lineTo(0.5769 * sketch_scale, 0.1768 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.6402 * sketch_scale), (0.0825 * sketch_scale, 0.6626 * sketch_scale))
    .lineTo(0.0825 * sketch_scale, 0.6563 * sketch_scale)
    .threePointArc((0.0406 * sketch_scale, 0.6751 * sketch_scale), (0.0825 * sketch_scale, 0.6626 * sketch_scale))
    .lineTo(0.0825 * sketch_scale, 0.5253 * sketch_scale)
    .threePointArc((0.0073
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1322.stl