import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate ---
part_1_length = 0.375 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.1125
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0062 * 0.0268  # Scaled radius
cylinder_height = 0.0078
# Cylinder positions (scaled and translated)
cylinder_positions = [
    (0.0062 * 0.0268 - part_1_length/2, 0.0062 * 0.0268 - part_1_width/2),
    (0.0062 * 0.0268 - part_1_length/2, 0.7395 * 0.0268 - part_1_width/2),
    (0.7395 * 0.0268 - part_1_length/2, 0.0062 * 0.0268 - part_1_width/2),
    (0.7395 * 0.02
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_805.stl