import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1462 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1308 * sketch_scale)
    .threePointArc((0.0489 * sketch_scale, 0.0352 * sketch_scale), (0.0577 * sketch_scale, 0.0188 * sketch_scale))
    .lineTo(0.6161 * sketch_scale, 0.0188 * sketch_scale)
    .threePointArc((0.7497 * sketch_scale, 0.0), (0.75 * sketch_scale, 0.0278 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2598 * sketch_scale)
    .threePointArc((0.7497 * sketch_scale, 0.2116 * sketch_scale), (0.5881 * sketch_scale, 0.2829 * sketch_scale))
    .lineTo(0.0954 * sketch_scale, 0.2829 * sketch_scale)
    .threePointArc((0.0489 * sketch_scale, 0.2116 * sketch_scale),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2014.stl