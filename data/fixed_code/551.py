import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate with Holes ---
part_1_length = 0.5966 * 0.5966  # Scaled length
part_1_width = 0.4432 * 0.5966  # Scaled width
part_1_height = 0.0426  # Height
hole_radius = 0.0298 * 0.5966  # Scaled radius
hole_centers = [
    (0.0562 * 0.5966 - part_1_length/2, 0.1172 * 0.5966 - part_1_width/2),
    (0.0562 * 0.5966 - part_1_length/2, 0.4634 * 0.5966 - part_1_width/2),
    (0.3594 * 0.5966 - part_1_length/2, 0.1172 * 0.5966 - part_1_width/2)
]
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
for center in hole_centers:
    part_1 = part_1.faces(">Z").workplane().pushPoints([center]).hole(2 * hole_radius)
# --- Part 2: Cylindrical Protrusions ---
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_551.stl