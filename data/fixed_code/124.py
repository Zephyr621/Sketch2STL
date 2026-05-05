import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3375 * 0.75  # Scaled width
part_1_height = 0.015
hole_radius = 0.0094 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .pushPoints([((0.0375 - part_1_length/2), (0.0375 - part_1_width/2))])
    .hole(hole_radius * 2)
)
# --- Part 2: Protruding Rectangular Section ---
part_2_x = 0.0125 * 0.3375  # Scaled x-coordinate
part_2_y = 0.0125 * 0.3375  # Scaled y-coordinate
part_2_z = 0.015
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_124.stl