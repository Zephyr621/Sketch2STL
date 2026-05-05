import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.4687
height = 0.0469
sketch_scale = 0.75
hole_radius = 0.0281
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole1_x = 0.1406 * sketch_scale - scaled_length/2
hole1_y = 0.1268 * sketch_scale - scaled_width/2
hole2_x = 0.6094 * sketch_scale - scaled_length/2
hole2_y = 0.1268 * sketch_scale - scaled_width/2
# --- Create the base shape ---
base = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length, 0)
    .threePointArc((scaled_length + (0.75-scaled_length)/2, 0.1051*sketch_scale), (scaled_length, 0.4687*sketch_scale))
    .lineTo(0, 0.4687*sketch
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3497.stl