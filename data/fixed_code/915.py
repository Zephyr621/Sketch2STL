import cadquery as cq
from math import *
# --- Part 1: Octagonal Plate ---
sketch_scale = 0.75
height = 0.0044
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.3248 * sketch_scale)
p2 = (0.1875 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.5625 * sketch_scale, 0.0 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.3248 * sketch_scale)
p5 = (0.5625 * sketch_scale, 0.6406 * sketch_scale)
p6 = (0.1875 * sketch_scale, 0.6406 * sketch_scale)
p7 = (0.0 * sketch_scale, 0.3248 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_915.stl