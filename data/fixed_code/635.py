import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.2499
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.3024 * sketch_scale)
    .threePointArc((0.0341 * sketch_scale, 0.0268 * sketch_scale), (0.0887 * sketch_scale, 0.0987 * sketch_scale))
    .lineTo(0.3267 * sketch_scale, 0.0536 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.0 * sketch_scale), (0.5806 * sketch_scale, 0.0874 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.6205 * sketch_scale)
    .threePointArc((0.7342 * sketch_scale, 0.5192 * sketch_scale), (0.5834 * sketch_scale, 0.4714 * sketch_scale))
    .lineTo(0.3337 * sketch_scale, 0.4714 * sketch_scale)
    .threePointArc((0.0469 * sketch_scale, 0.5226
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_635.stl