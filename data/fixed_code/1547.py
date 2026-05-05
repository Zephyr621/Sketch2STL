import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangular Prism ---
sketch_scale = 0.75
extrude_depth = 0.2209
# Scaled coordinates for the triangle
p1 = (0.0 * sketch_scale, 0.1579 * sketch_scale)
p2 = (0.375 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.75 * sketch_scale, 0.1579 * sketch_scale)
p4 = (0.6321 * sketch_scale, 0.3068 * sketch_scale)
p5 = (0.375 * sketch_scale, 0.3024 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.3024 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc((0.375 * sketch_scale, 0.1403 * sketch_scale), p2)
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .lineTo(p5[0], p5[1])
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1547.stl