import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0124
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0364 * sketch_scale, 0)
    .lineTo(0.7059 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.1348 * sketch_scale), (0.7059 * sketch_scale, 0.4262 * sketch_scale))
    .lineTo(0.0364 * sketch_scale, 0.4262 * sketch_scale)
    .threePointArc((0, 0.1348 * sketch_scale), (0.0364 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_centers = [
    (0.0364 * sketch_scale, 0.1875 * sketch_scale),
    (0.5643 * sketch_scale, 0.0364 * sketch_scale),
    (0.5643 * sketch_scale, 0.375 * sketch_scale),
    (0.7059 * sketch_scale, 0.375 * sketch_scale)
]
for center_x, center_y in hole_centers:
    part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3320.stl