import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0052 * sketch_scale, 0.0156 * sketch_scale)
    .threePointArc((0.0037 * sketch_scale, 0.0038 * sketch_scale), (0.0052 * sketch_scale, 0.0))
    .lineTo(0.7083 * sketch_scale, 0.0)
    .threePointArc((0.7428 * sketch_scale, 0.0038 * sketch_scale), (0.75 * sketch_scale, 0.0156 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1579 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.2259 * sketch_scale), (0.7083 * sketch_scale, 0.1579 * sketch_scale))
    .lineTo(0.7083 * sketch_scale, 0.3 * sketch_scale)
    .threePointArc((0.7428 * sketch_scale, 0.1986 * sketch_scale), (0.7083
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2712.stl