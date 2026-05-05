import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Bone-shaped Object ---
sketch_scale = 0.75
# Scaled coordinates for the sketch
p1 = (0.0 * sketch_scale, 0.0 * sketch_scale)
p2 = (0.1938 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.75 * sketch_scale, 0.1875 * sketch_scale)
p4 = (0.6875 * sketch_scale, 0.5 * sketch_scale)
p5 = (0.3562 * sketch_scale, 0.5 * sketch_scale)
p6 = (0.1938 * sketch_scale, 0.5 * sketch_scale)
p7 = (0.0 * sketch_scale, 0.0 * sketch_scale)
mid_arc1 = (0.375 * sketch_scale, 0.1773 * sketch_scale)
mid_arc2 = (0.3359 * sketch_scale, 0.1607 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .threePointArc(mid_arc1, p3)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_454.stl