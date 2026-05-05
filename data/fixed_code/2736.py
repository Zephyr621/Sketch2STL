import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1971 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1601 * sketch_scale)
    .threePointArc((0.0225 * sketch_scale, 0.0225 * sketch_scale), (0.1601 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.6342 * sketch_scale)
    .lineTo(0.5833 * sketch_scale, 0.6342 * sketch_scale)
    .lineTo(0.5833 * sketch_scale, 0.3268 * sketch_scale)
    .threePointArc((0.7232 * sketch_scale, 0.4851 * sketch_scale), (0.5833 * sketch_scale, 0.6563 * sketch_scale))
    .lineTo(0.1601 * sketch_scale, 0.6494 * sketch
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2736.stl