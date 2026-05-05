import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1875 * 2  # Total extrusion depth (both directions)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0107 * sketch_scale)
    .threePointArc((0.0035 * sketch_scale, 0.0035 * sketch_scale), (0.0107 * sketch_scale, 0.0))
    .lineTo(0.7269 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.0035 * sketch_scale), (0.75 * sketch_scale, 0.0107 * sketch_scale))
    .lineTo(0.7031 * sketch_scale, 0.0107 * sketch_scale)
    .threePointArc((0.7415 * sketch_scale, 0.0035 * sketch_scale), (0.7031 * sketch_scale, 0.0268 * sketch_scale))
    .lineTo(0.7031 * sketch_scale, 0.6178 * sketch_scale)
    .threePointArc((0.7415 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_962.stl