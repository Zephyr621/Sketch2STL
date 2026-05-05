import cadquery as cq
from math import *
# --- Parameters from JSON ---
length = 0.75
width = 0.4773
height = 0.0125
sketch_scale = 0.75
hole_radius = 0.0281
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole_centers = [
    (0.0443 * sketch_scale - scaled_length/2, 0.0443 * sketch_scale - scaled_width/2),
    (0.0443 * sketch_scale - scaled_length/2, 0.2885 * sketch_scale - scaled_width/2),
    (0.7258 * sketch_scale - scaled_length/2, 0.0443 * sketch_scale - scaled_width/2),
    (0.7258 * sketch_scale - scaled_length/2, 0.2885 * sketch_scale - scaled_width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(scaled_length, scaled_width).extrude(scaled_height)
# --- Add the holes ---
for center_x, center_y in hole_
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3445.stl