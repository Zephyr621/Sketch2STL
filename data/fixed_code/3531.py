import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.4207
height = 0.0085
sketch_scale = 0.75
hole_radius = 0.0085
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole_centers = [
    (0.0458 * sketch_scale - scaled_length / 2, 0.0273 * sketch_scale - scaled_width / 2),
    (0.0458 * sketch_scale - scaled_length / 2, 0.3526 * sketch_scale - scaled_width / 2),
    (0.7083 * sketch_scale - scaled_length / 2, 0.0273 * sketch_scale - scaled_width / 2),
    (0.7083 * sketch_scale - scaled_length / 2, 0.3526 * sketch_scale - scaled_width / 2)
]
# --- Create the base plate ---
plate = cq.Workplane("XY").rect(scaled_length, scaled_width).extrude(scaled_height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3531.stl