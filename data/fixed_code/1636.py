import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: S shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.0144 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.1763 * sketch_scale)
    .threePointArc((0.0089 * sketch_scale, 0.0089 * sketch_scale), (0.0023 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.375 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.0089 * sketch_scale), (0.75 * sketch_scale, 0.1763 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.3586 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.7316 * sketch_scale), (0.375 * sketch_scale, 0.7263 * sketch_scale))
    .lineTo(0.0023 * sketch_scale, 0.7263 * sketch_scale)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1636.stl