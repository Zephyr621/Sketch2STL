import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.4286 * sketch_scale
# Define the points for the sketch (scaled)
p1 = (0.0 * sketch_scale, 0.3214 * sketch_scale)
p2 = (0.375 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.75 * sketch_scale, 0.3214 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.6429 * sketch_scale)
p5 = (0.375 * sketch_scale, 0.6429 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.6429 * sketch_scale)
# Create the sketch using the scaled coordinates
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc((0.375 * sketch_scale, 0.3357 * sketch_scale), (p2[0], p2[1]))
    .lineTo(p3[0], p3[1])
    .threePointArc((0.375 * sketch_scale, 0.6571 * sketch_scale), (p4[0], p4[1]))
    .lineTo(p5[0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3377.stl