import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0017 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7102 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.0029 * sketch_scale), (0.7102 * sketch_scale, 0.0577 * sketch_scale))
    .lineTo(0.0458 * sketch_scale, 0.0577 * sketch_scale)
    .threePointArc((0.0346 * sketch_scale, 0.0029 * sketch_scale), (0.0309 * sketch_scale, 0.0577 * sketch_scale))
    .lineTo(0.0234 * sketch_scale, 0.0577 * sketch_scale)
    .threePointArc((0.0137 * sketch_scale, 0.0029 * sketch_scale), (0.0, 0.0577 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2897.stl