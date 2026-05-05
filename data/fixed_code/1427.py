import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0083 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0424 * sketch_scale)
    .lineTo(0.0013 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0941 * sketch_scale), (0.7125 * sketch_scale, 0.0848 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0521 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.1927 * sketch_scale)
    .lineTo(0.0013 * sketch_scale, 0.1927 * sketch_scale)
    .lineTo(0.0, 0.0424 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_radius = 0.0112 * sketch_scale
part_1 = part_1.faces(">Z").workplane().hole(2 * hole_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0395, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1427.stl