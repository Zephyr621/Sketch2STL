import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.75
height = 0.2462
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.3248 * sketch_scale)
p2 = (0.3248 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.6495 * sketch_scale, 0.1875 * sketch_scale)
p4 = (0.6495 * sketch_scale, 0.5625 * sketch_scale)
p5 = (0.3248 * sketch_scale, 0.75 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.5625 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .lineTo(p5[0], p5[1])
    .lineTo(p6[0], p6[1])
    .close()
    .extrude(height)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3104.stl