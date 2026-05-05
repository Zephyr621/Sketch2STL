import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1875 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0312 * sketch_scale), (0.75 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.125 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.2453 * sketch_scale), (0.0, 0.125 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2998.stl