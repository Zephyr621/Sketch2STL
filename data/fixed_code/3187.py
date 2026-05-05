import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0074 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0074 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.2537 * sketch_scale), (0.7423 * sketch_scale, 0.4446 * sketch_scale))
    .lineTo(0.7423 * sketch_scale, 0.4921 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.5672 * sketch_scale), (0.0, 0.4921 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .moveTo(0.0074 * sketch_scale, 0.0147 * sketch_scale)
    .circle(0.0047 * sketch_scale)
    .extrude(-extrude_depth)
)
# Add holes
hole_center1 = (0.0074 * sketch_scale, 0.0074 * sketch_scale)
hole_center2 = (0.7423 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3187.stl