import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0469 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0039 * sketch_scale)
    .lineTo(0.0702 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0469 * sketch_scale), (0.6765 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0039 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.2667 * sketch_scale)
    .lineTo(0.7395 * sketch_scale, 0.4687 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.4687 * sketch_scale), (0.1482 * sketch_scale, 0.4687 * sketch_scale))
    .lineTo(0.0, 0.2667 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_694.stl