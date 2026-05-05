import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.3606 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0033 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.1504 * sketch_scale), (0.7188 * sketch_scale, 0))
    .lineTo(0.75 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.1663 * sketch_scale), (0.7188 * sketch_scale, 0.3214 * sketch_scale))
    .lineTo(0.0033 * sketch_scale, 0.3214 * sketch_scale)
    .threePointArc((0, 0.1663 * sketch_scale), (0.0033 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1535.stl