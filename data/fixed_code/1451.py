import cadquery as cq
from math import *
# --- Part 1: Square Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6716 * 0.75  # Scaled width
part_1_height = 0.0269
hole_radius = 0.0117 * 0.75  # Scaled radius
corner_offset = 0.0586 * 0.75  # Scaled offset for corner
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([
        (corner_offset - part_1_length / 2, corner_offset - part_1_width / 2),
        (corner_offset - part_1_length / 2, part_1_width / 2 - corner_offset),
        (part_1_length / 2 - corner_offset, part_1_width / 2 - corner_offset)
    ])
    .hole(2 * hole_radius)
)
# --- Part 2: L-shaped Extension ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.6716 * 0.75  # Scal
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1451.stl