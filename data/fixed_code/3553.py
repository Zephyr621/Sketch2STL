import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.4375
height = 0.0225
sketch_scale = 0.75
hole_radius = 0.0112 * sketch_scale
corner_radius = 0.1062 * sketch_scale
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
# Hole centers (scaled)
hole1_x = 0.0562 * sketch_scale
hole1_y = 0.0618 * sketch_scale
hole2_x = 0.6989 * sketch_scale
hole2_y = 0.0618 * sketch_scale
hole3_x = 0.6773 * sketch_scale
hole3_y = 0.0618 * sketch_scale
hole4_x = 0.7125 * sketch_scale
hole4_y = 0.0618 * sketch_scale
# --- Create the base shape ---
base = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .lineTo(scaled_length - corner_radius, 0)
    .threePointArc((scaled_length, corner_radius), (scaled_length, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3553.stl