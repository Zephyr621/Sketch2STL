import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.0675
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0078 * sketch_scale, 0)
    .threePointArc((0.0013 * sketch_scale, 0.0013 * sketch_scale), (0.0078 * sketch_scale, 0.0233 * sketch_scale))
    .lineTo(0.0675 * sketch_scale, 0.0233 * sketch_scale)
    .threePointArc((0.0013 * sketch_scale, 0.0149 * sketch_scale), (0.0078 * sketch_scale, 0.0098 * sketch_scale))
    .lineTo(0.0078 * sketch_scale, 0.0098 * sketch_scale)
    .threePointArc((0.0013 * sketch_scale, 0.0149 * sketch_scale), (0.0078 * sketch_scale, 0.0061 * sketch_scale))
    .lineTo(0.0078 * sketch_scale, 0.0061 * sketch_scale)
    .threePointArc((0.0013 * sketch_scale, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1864.stl