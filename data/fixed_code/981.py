import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.5
height = 0.0235
sketch_scale = 0.75
hole_radius = 0.0058 * sketch_scale
corner_radius = 0.0511 * sketch_scale
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole_center1 = (0.0511 * sketch_scale - scaled_length/2, 0.0511 * sketch_scale - scaled_width/2)
hole_center2 = (0.6957 * sketch_scale - scaled_length/2, 0.0511 * sketch_scale - scaled_width/2)
hole_center3 = (0.7143 * sketch_scale - scaled_length/2, 0.0511 * sketch_scale - scaled_width/2)
hole_center4 = (0.7143 * sketch_scale - scaled_length/2, 0.6771 * sketch_scale - scaled_width/2)
# --- Create the base plate ---
plate = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .threePointArc((corner_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_981.stl