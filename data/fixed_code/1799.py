import cadquery as cq
import math
from cadquery import exporters
# --- Parameters from JSON ---
length = 0.75
width = 0.2188
height = 0.0225
sketch_scale = 0.75
hole_radius = 0.0158 * sketch_scale
corner_radius = 0.0562 * sketch_scale
# Scaled hole centers relative to the center of the rectangle
hole_centers = [
    (0.0259 * sketch_scale, 0.0231 * sketch_scale),
    (0.0259 * sketch_scale, 0.1134 * sketch_scale),
    (0.6867 * sketch_scale, 0.0231 * sketch_scale)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Cut out the corner holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x - (length * sketch_scale)/2, center_y - (width * sketch_scale)/2)]).hole(2 * hole_radius)
# --- Apply rotation and translation ---
plate = plate.rotate((0, 0, 0), (1, 0, 0), -90)
plate = plate.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Export to STL ---
# --- Export to STL
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1799.stl