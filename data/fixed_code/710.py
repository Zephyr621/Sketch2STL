import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.0293
extrude_depth = 0.75
# Scaled coordinates for the sketch
p1 = (0.0037 * sketch_scale, 0.0037 * sketch_scale)
p2 = (0.0234 * sketch_scale, 0.0037 * sketch_scale)
p3 = (0.0234 * sketch_scale, 0.0155 * sketch_scale)
p4 = (0.0234 * sketch_scale, 0.0155 * sketch_scale)
p5 = (0.0037 * sketch_scale, 0.0155 * sketch_scale)
p6 = (0.0037 * sketch_scale, 0.0155 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc((0, 0), (p2[0], p2[1]))
    .lineTo(p3[0], p3[1])
    .threePointArc((0.0232 * sketch_scale, 0.0166 * sketch_scale), (p4[0], p4[1]))
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_710.stl