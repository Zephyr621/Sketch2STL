import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0469 * sketch_scale
width = 0.4687 * sketch_scale
length = 0.75 * sketch_scale
radius = 0.2344 * sketch_scale
hole1_center = (0.1222 * sketch_scale, 0.1288 * sketch_scale)
hole2_center = (0.6161 * sketch_scale, 0.1288 * sketch_scale)
hole3_center = (0.6161 * sketch_scale, 0.2438 * sketch_scale)
hole_radius = 0.0131 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1222 * sketch_scale, 0)
    .lineTo(0.7498 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.2344 * sketch_scale), (0.7498 * sketch_scale, 0.4687 * sketch_scale))
    .lineTo(0.1222 * sketch_scale, 0.4687 * sketch_scale)
    .threePointArc((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_154.stl