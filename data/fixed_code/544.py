import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.0687 * sketch_scale
# Scaled coordinates for the sketch
p1 = (0.0 * sketch_scale, 0.0068 * sketch_scale)
p2 = (0.0134 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.7159 * sketch_scale, 0.0068 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.2088 * sketch_scale)
p5 = (0.7159 * sketch_scale, 0.2204 * sketch_scale)
p6 = (0.0134 * sketch_scale, 0.2204 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .threePointArc((0.375 * sketch_scale, 0.0 * sketch_scale), (p3[0], p3[1]))
    .lineTo(p4[0], p4[1])
    .threePointArc((0.375 * sketch_scale, 0.1058 * sketch_scale), (p5[0], p5[1]))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_544.stl