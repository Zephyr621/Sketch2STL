import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.2454
# Scaled dimensions
p1 = (0.0 * sketch_scale, 0.1966 * sketch_scale)
p2 = (0.2727 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.4733 * sketch_scale, 0.1798 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.1574 * sketch_scale)
p5 = (0.6194 * sketch_scale, 0.4465 * sketch_scale)
p6 = (0.3751 * sketch_scale, 0.4399 * sketch_scale)
p7 = (0.0 * sketch_scale, 0.4465 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .threePointArc((0.375 * sketch_scale, 0.2618 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_558.stl