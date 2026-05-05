import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Bracket ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2386 * sketch_scale
height = 0.0536
hole_radius = 0.0268 * sketch_scale
# Scaled dimensions
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole1_x = 0.0789 * sketch_scale
hole2_x = 0.6798 * sketch_scale
hole3_x = 0.6094 * sketch_scale
hole4_x = 0.6495 * sketch_scale
# Create the base shape with rounded edges
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length - scaled_length/2, 0)
    .threePointArc((scaled_length, scaled_width), (scaled_length - scaled_length/2, scaled_width))
    .lineTo(scaled_length, scaled_width)
    .threePointArc((scaled_length - scaled_length/2, scaled_width + scaled_arc1_radius), (scaled_length - scaled_length/2, scaled_width))
    .lineTo(0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2701.stl