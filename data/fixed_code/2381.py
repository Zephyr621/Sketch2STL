import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.5357
height = 0.0107
sketch_scale = 0.75
hole_radius = 0.0058 * sketch_scale
corner_radius = 0.0268 * sketch_scale
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
# Hole centers (scaled)
hole_centers = [
    (0.1071 * sketch_scale - scaled_length / 2, 0.3214 * sketch_scale - scaled_width / 2),
    (0.6429 * sketch_scale - scaled_length / 2, 0.3214 * sketch_scale - scaled_width / 2),
    (0.6429 * sketch_scale - scaled_length / 2, 0.5357 * sketch_scale - scaled_width / 2),
    (0.6429 * sketch_scale - scaled_length / 2, 0.5357 * sketch_scale - scaled_width / 2)
]
# --- Create the base plate ---
plate = cq.Workplane("XY").rect(scaled_length, scaled_width).extrude(scaled_height)
# --- Cut the holes ---
for center_x, center
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2381.stl