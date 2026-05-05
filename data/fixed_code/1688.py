import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
outer_width = 0.6495 * 0.75
inner_radius = 0.1625 * 0.75
height = 0.1269
sketch_scale = 0.75
# Scaled dimensions
scaled_outer_width = outer_width * sketch_scale
scaled_inner_radius = inner_radius * sketch_scale
scaled_height = height
# Scaled hole centers (scaled)
hole1_center = (0.125 * sketch_scale, 0.3248 * sketch_scale)
hole2_center = (0.625 * sketch_scale, 0.3248 * sketch_scale)
hole_radius = 0.0625 * sketch_scale
# --- Create the Hexagonal Nut ---
hex_nut = (
    cq.Workplane("XY")
    .moveTo(0.0, scaled_height/2)
    .lineTo(scaled_outer_width - scaled_width/2, 0.0)
    .lineTo(scaled_outer_width, scaled_height/2)
    .threePointArc((scaled_width/2, scaled_height/2), (scaled_outer_width, scaled_height))
    .close()
    .extrude(scaled_height)
)
# --- Create the Hole ---
hex_nut = (
    hex_nut.faces(">Z")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1688.stl