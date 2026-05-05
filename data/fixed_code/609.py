import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1928 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5294 * sketch_scale)
    .threePointArc((0.0038 * sketch_scale, 0.0038 * sketch_scale), (0.375 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.7286 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.7214 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.7214 * sketch_scale, 0.5294 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.5294 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Create holes
hole_radius = 0.0536 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([(0.1885 * sketch_scale - (0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_609.stl