import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0816 * sketch_scale
# Scaled dimensions
arc_radius = 0.0417 * sketch_scale
length = 0.75 * sketch_scale
width = 0.2753 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.0074 * sketch_scale, 0.0074 * sketch_scale))
    .lineTo(length - arc_radius, 0)
    .threePointArc((length, arc_radius), (length - 0.0074 * sketch_scale, 0.0074 * sketch_scale))
    .lineTo(length, width - arc_radius)
    .threePointArc((length - arc_radius, width), (length - 0.0074 * sketch_scale, width - 0.0074 * sketch_scale))
    .lineTo(arc_radius, width)
    .threePointArc((0, width - arc_radius), (0.0074 * sketch_scale, width - 0.00
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1255.stl