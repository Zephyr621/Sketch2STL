import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0283 * sketch_scale
# Scaled coordinates for the sketch
p1 = (0.0 * sketch_scale, 0.0045 * sketch_scale)
p2 = (0.1357 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.6281 * sketch_scale, 0.0045 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.0045 * sketch_scale)
p5 = (0.7295 * sketch_scale, 0.0189 * sketch_scale)
p6 = (0.75 * sketch_scale, 0.0316 * sketch_scale)
p7 = (0.7295 * sketch_scale, 0.0458 * sketch_scale)
p8 = (0.0 * sketch_scale, 0.0316 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc(p2, p3)
    .lineTo(p4[0], p4[1])
    .threePointArc(p5, p6)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1194.stl