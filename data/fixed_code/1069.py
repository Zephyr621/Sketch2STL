import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Corners ---
sketch_scale = 0.75
# Scaled Dimensions
arc_radius = 0.0125 * sketch_scale
hole_radius = 0.0058 * sketch_scale
corner_radius = 0.0112 * sketch_scale
hole_centers = [
    (0.0112 * sketch_scale - arc_radius, 0),
    (0.0112 * sketch_scale - arc_radius, 0.7395 * sketch_scale - arc_radius),
    (0.7395 * sketch_scale - arc_radius, 0),
    (0.7395 * sketch_scale - arc_radius, 0.7395 * sketch_scale - arc_radius)
]
# Create the base shape with rounded corners
part_1 = (
    cq.Workplane("XY")
    .moveTo(corner_radius, 0)
    .lineTo(0.0112 * sketch_scale, 0)
    .threePointArc((0.0124 * sketch_scale, corner_radius), (0.0112 * sketch_scale, 0.7395 * sketch_scale))
    .lineTo(corner_radius, 0.7395
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1069.stl