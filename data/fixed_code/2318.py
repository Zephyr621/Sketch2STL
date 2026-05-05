import cadquery as cq
from math import radians
# --- Part 1: Square Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.0391
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
)
# --- Part 2: Holes ---
hole_radius = 0.0059 * 0.6781
hole_depth = 0.7143
hole_centers = [
    (0.0059 * 0.6781 - plate_length/2, 0.0059 * 0.6781 - plate_width/2),
    (0.0059 * 0.6781 - plate_length/2, 0.6783 * 0.6781 - plate_width/2),
    (0.7143 * 0.6781 - plate_length/2, 0.0059 * 0.6781 - plate_width/2),
    (0.7143 * 0.6781 - plate_length/2, 0.6783 * 0.6781 - plate_width/2)
]
# Create holes
for x, y in hole_centers:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2318.stl