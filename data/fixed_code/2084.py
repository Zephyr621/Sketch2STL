import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1091 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0565 * sketch_scale)
    .threePointArc((0.0039 * sketch_scale, 0.0039 * sketch_scale), (0.0565 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .threePointArc((0.7354 * sketch_scale, 0.0039 * sketch_scale), (0.6951 * sketch_scale, 0.0565 * sketch_scale))
    .lineTo(0.6829 * sketch_scale, 0.2813 * sketch_scale)
    .threePointArc((0.7354 * sketch_scale, 0.2753 * sketch_scale), (0.6829 * sketch_scale, 0.2893 * sketch_scale))
    .lineTo(0.0565 * sketch_scale, 0.2893 * sketch_scale)
    .threePointArc((0.0039 * sketch_scale, 0.2753 * sketch_scale), (0.0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2084.stl