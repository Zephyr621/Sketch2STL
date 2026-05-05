import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0109
# Scaled dimensions
arc_radius = 0.0365 * sketch_scale
line_length = 0.6857 * sketch_scale
total_width = 0.5595 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(line_length, 0)
    .threePointArc((line_length + arc_radius, line_length), (line_length, total_width))
    .lineTo(line_length - arc_radius, total_width)
    .threePointArc((line_length + arc_radius, line_length - arc_radius), (line_length, total_width - 2 * arc_radius))
    .lineTo(line_length, total_width)
    .threePointArc((line_length - arc_radius, line_length - arc_radius), (line_length - arc_radius, line_length))
    .lineTo(line_length, total_width)
    .threePointArc((line_length - arc_radius
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2429.stl