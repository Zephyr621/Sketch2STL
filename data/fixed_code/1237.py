import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0536 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7382 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.1262 * sketch_scale), (0.7382 * sketch_scale, 0.2524 * sketch_scale))
    .lineTo(0.0, 0.2524 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .add(cq.Workplane("XY").circle(0.0207 * sketch_scale).val().move(cq.Location(cq.Vector(0.0079 * sketch_scale, 0.1262 * sketch_scale, 0))))
    .extrude(extrude_depth)
)
# Add holes
hole_radius = 0.0058 * sketch_scale
hole_centers = [
    (0.0057 * sketch_scale - 0.04
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1237.stl