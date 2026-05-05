import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.6814 * sketch_scale
height = 0.1894
# Scaled dimensions
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length, 0)
    .lineTo(scaled_length, scaled_width)
    .threePointArc((scaled_length/2, scaled_width/2), (0, scaled_width))
    .lineTo(0, 0)
    .close()
    .extrude(height)
)
# Create holes
hole_radius = 0.0141 * sketch_scale
hole_center_x = 0.375 * sketch_scale - scaled_length/2
hole_center_y = 0.3167 * sketch_scale - scaled_width/2
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x, hole_center_y)]).hole(2 * hole_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1209.stl