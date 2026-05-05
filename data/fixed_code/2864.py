import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.2143 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0916 * sketch_scale)
    .threePointArc((0.0023 * sketch_scale, 0.0023 * sketch_scale), (0.0916 * sketch_scale, 0.0))
    .lineTo(0.6958 * sketch_scale, 0.0)
    .threePointArc((0.7425 * sketch_scale, 0.0023 * sketch_scale), (0.75 * sketch_scale, 0.0916 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2704 * sketch_scale)
    .threePointArc((0.7425 * sketch_scale, 0.3088 * sketch_scale), (0.6958 * sketch_scale, 0.3047 * sketch_scale))
    .lineTo(0.0529 * sketch_scale, 0.3047 * sketch_scale)
    .threePointArc((0.0277 * sketch_scale, 0.3088 * sketch
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2864.stl