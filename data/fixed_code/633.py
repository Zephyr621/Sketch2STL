import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0168 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0477 * sketch_scale, 0)
    .lineTo(0.6346 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.0317 * sketch_scale), (0.6965 * sketch_scale, 0.0742 * sketch_scale))
    .lineTo(0.7498 * sketch_scale, 0.0742 * sketch_scale)
    .threePointArc((0.7479 * sketch_scale, 0.0317 * sketch_scale), (0.6702 * sketch_scale, 0.0742 * sketch_scale))
    .lineTo(0.6702 * sketch_scale, 0.0477 * sketch_scale)
    .threePointArc((0.7479 * sketch_scale, 0.0938 * sketch_scale), (0.6965 * sketch_scale, 0.0937 * sketch_scale))
    .lineTo(0.0477 * sketch_scale, 0.0937 * sketch_scale)
    .threePointArc((0, 0.0317 * sketch_scale), (0.0477
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_633.stl