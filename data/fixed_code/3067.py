import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0375
# Scaled dimensions
arc_radius = 0.0274 * sketch_scale
length = 0.7188 * sketch_scale
width = 0.75 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.0188 * sketch_scale, 0.0188 * sketch_scale))
    .lineTo(length - arc_radius, 0)
    .threePointArc((length, arc_radius), (0.7188 * sketch_scale, 0.0188 * sketch_scale))
    .lineTo(length, width - arc_radius)
    .threePointArc((length - arc_radius, width), (0.7188 * sketch_scale, 0.7188 * sketch_scale))
    .lineTo(arc_radius, width)
    .threePointArc((0, width - arc_radius), (0.0188 * sketch_scale, 0.7188 * sketch_scale))
    .close()
    .extrude(-extrude_depth)
)
# --- Coordinate System Transformation
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3067.stl