import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Edges ---
sketch_scale = 0.75
extrude_depth = 0.0536 * sketch_scale
# Scaled coordinates for the sketch
start_point = (0.2779 * sketch_scale, 0)
mid_point = (0.375 * sketch_scale, 0.3355 * sketch_scale)
end_point = (0.2779 * sketch_scale, 0.2917 * sketch_scale)
line1_end_x = 0.2779 * sketch_scale
line1_end_y = 0.2917 * sketch_scale
arc2_mid_x = 0.375 * sketch_scale
arc2_mid_y = 0.3281 * sketch_scale
line2_end_x = 0.2779 * sketch_scale
line2_end_y = 0.2917 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(start_point[0], start_point[1])
    .threePointArc(mid_point, end_point)
    .lineTo(line1_end_x, line1_end_y)
    .threePointArc(mid_point, line2_end_x
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3247.stl