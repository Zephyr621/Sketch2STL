import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.2669 * 2  # Total extrusion depth (both directions)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0061 * sketch_scale)
    .lineTo(0.7353 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0129 * sketch_scale)
    .lineTo(0.7353 * sketch_scale, 0.4375 * sketch_scale)
    .threePointArc((0.7413 * sketch_scale, 0.2344 * sketch_scale), (0.7353 * sketch_scale, 0.4725 * sketch_scale))
    .lineTo(0.0, 0.4826 * sketch_scale)
    .lineTo(0.0, 0.0061 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_899.stl