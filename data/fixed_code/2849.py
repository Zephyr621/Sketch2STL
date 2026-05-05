import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.4687 * sketch_scale
# Scaled coordinates for the sketch
p1 = (0.0 * sketch_scale, 0.3715 * sketch_scale)
p2 = (0.0741 * sketch_scale, 0.3715 * sketch_scale)
p3 = (0.0424 * sketch_scale, 0.6136 * sketch_scale)
p4 = (0.0912 * sketch_scale, 0.6136 * sketch_scale)
p5 = (0.1389 * sketch_scale, 0.3715 * sketch_scale)
p6 = (0.1084 * sketch_scale, 0.375 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .threePointArc((0.1337 * sketch_scale, 0.0856 * sketch_scale), p3)
    .lineTo(p4[0], p4[1])
    .threePointArc((0.1323 * sketch_scale, 0.075 * sketch_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2849.stl