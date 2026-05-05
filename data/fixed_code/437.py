import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0227 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0031 * sketch_scale, 0.0105 * sketch_scale)
    .threePointArc((0.0026 * sketch_scale, 0.0026 * sketch_scale), (0.0031 * sketch_scale, 0.0))
    .lineTo(0.7159 * sketch_scale, 0.0)
    .threePointArc((0.7416 * sketch_scale, 0.0026 * sketch_scale), (0.75 * sketch_scale, 0.0105 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2714 * sketch_scale)
    .threePointArc((0.7416 * sketch_scale, 0.2432 * sketch_scale), (0.7159 * sketch_scale, 0.2586 * sketch_scale))
    .lineTo(0.0031 * sketch_scale, 0.2586 * sketch_scale)
    .threePointArc((0.0026 * sketch_scale, 0.2432 * sketch_scale), (0.0031
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_437.stl