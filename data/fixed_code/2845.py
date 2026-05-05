import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.2143 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0107 * sketch_scale)
    .threePointArc((0.0066 * sketch_scale, 0.0066 * sketch_scale), (0.0107 * sketch_scale, 0.0))
    .lineTo(0.7143 * sketch_scale, 0.0)
    .threePointArc((0.7416 * sketch_scale, 0.0066 * sketch_scale), (0.75 * sketch_scale, 0.0107 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.7232 * sketch_scale)
    .threePointArc((0.7416 * sketch_scale, 0.7416 * sketch_scale), (0.7143 * sketch_scale, 0.75 * sketch_scale))
    .lineTo(0.0107 * sketch_scale, 0.75 * sketch_scale)
    .threePointArc((0.0066 * sketch_scale,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2845.stl