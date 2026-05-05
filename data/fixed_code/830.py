import cadquery as cq
from math import radians, pi, sin, cos, sqrt
import math
from cadquery.vis import show
# --- Part 1: Fidget Spinner ---
sketch_scale = 0.75
extrude_depth = 0.0116
# Scaled coordinates for the outer profile
outer_points = [
    (0.0479 * sketch_scale, 0.1469 * sketch_scale),
    (0.0799 * sketch_scale, 0.0208 * sketch_scale),
    (0.2926 * sketch_scale, 0.0396 * sketch_scale),
    (0.6643 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.2356 * sketch_scale)
]
# Scaled center coordinates for the inner profile
inner_center1 = (0.0459 * sketch_scale, 0.0625 * sketch_scale)
inner_center2 = (0.6798 * sketch_scale, 0.0625 * sketch_scale)
inner_radius = 0.0118 * sketch_scale
# Create the outer profile with arcs
part_1 = (
    cq.Workplane("XY")
    .moveTo(outer_points[0][0], outer_points[0][1])
    .threePointArc((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_830.stl