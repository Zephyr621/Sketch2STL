import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4507 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0393
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# Holes in Part 1
hole_centers = [
    (0.0562 * 0.75 - part_1_length / 2, 0.0562 * 0.75 - part_1_width / 2),
    (0.0562 * 0.75 - part_1_length / 2, 0.6923 * 0.75 - part_1_width / 2),
    (0.6923 * 0.75 - part_1_length / 2, 0.0562 * 0.75 - part_1_width / 2),
    (0.6923 * 0.75 - part_1_length / 2, 0.6923 * 0.75 - part_1_width / 2)
]
for center_x, center_y in hole_centers:
    part_1 = part_1.faces(">Z").workplane
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_516.stl