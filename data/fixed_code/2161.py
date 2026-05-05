import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0131 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0014 * sketch_scale)
    .threePointArc((0.0046 * sketch_scale, 0.0046 * sketch_scale), (0.0014 * sketch_scale, 0.0))
    .lineTo(0.7345 * sketch_scale, 0.0)
    .threePointArc((0.7425 * sketch_scale, 0.0046 * sketch_scale), (0.75 * sketch_scale, 0.0014 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1838 * sketch_scale)
    .lineTo(0.7345 * sketch_scale, 0.1838 * sketch_scale)
    .threePointArc((0.7425 * sketch_scale, 0.1386 * sketch_scale), (0.7345 * sketch_scale, 0.1793
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2161.stl