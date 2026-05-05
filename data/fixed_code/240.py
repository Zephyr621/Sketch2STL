import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0522 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.5446 * sketch_scale, 0.0)
    .threePointArc((0.4351 * sketch_scale, 0.0311 * sketch_scale), (0.5407 * sketch_scale, 0.0313 * sketch_scale))
    .lineTo(0.4872 * sketch_scale, 0.0469 * sketch_scale)
    .threePointArc((0.2736 * sketch_scale, 0.0542 * sketch_scale), (0.2786 * sketch_scale, 0.0834 * sketch_scale))
    .lineTo(0.2786 * sketch_scale, 0.1839 * sketch_scale)
    .threePointArc((0.2515 * sketch_scale, 0.375 * sketch_scale), (0.0962 * sketch_scale, 0.5402 * sketch_scale))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_240.stl