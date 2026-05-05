import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.45 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.375
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cutout ---
part_2_length = 0.2796 * 0.5272
part_2_width = 0.5272 * 0.5272
part_2_height = 0.1965
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
part_2 = part_2.translate((0.15, 0.0, 0.375))
# --- Part 3: Hole ---
part_3_radius = 0.0938 * 0.1875
part_3_depth = 1.5
part_3 = cq.Workplane("XY").circle(part_3_
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_1219.stl