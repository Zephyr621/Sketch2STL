import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75
part_1_width = 0.525 * 0.75
part_1_height = 0.195
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
part_1 = part_1.translate((0, 0, part_1_height))
# --- Part 2: Cube (Cut) ---
part_2_size = 0.15 * 0.45
part_2_depth = 0.12
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_depth)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.075, 0.0675, 0))
# --- Part 3: Cylinder (Hole) ---
part_3_radius = 0.015 * 0.3
part_3_depth = 0.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3410.stl