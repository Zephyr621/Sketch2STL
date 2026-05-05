import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Rounded Corners ---
sketch_scale = 0.75
extrude_depth = 0.0337 * sketch_scale
# Scaled dimensions
arc_radius = 0.0572 * sketch_scale
line_length = 0.6964 * sketch_scale
total_width = 0.2577 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.0572 * sketch_scale, 0.0572 * sketch_scale))
    .lineTo(line_length - arc_radius, 0)
    .threePointArc((line_length, arc_radius), (0.0572 * sketch_scale, 0.0572 * sketch_scale))
    .lineTo(line_length, total_width - arc_radius)
    .threePointArc((total_width, total_width), (0.0572 * sketch_scale, 0.2577 * sketch_scale))
    .lineTo(arc_radius, total_width)
    .threePointArc((0, total_width - arc_radius), (0.0572 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3438.stl