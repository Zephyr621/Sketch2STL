import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0625
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Part 2: Cut Cylinders ---
cut_radius = 0.03 * 0.06  # Sketch radius scaled
cut_depth = 0.0625
cut_locations = [
    (0.03 * 0.06, 0.03 * 0.06),
    (0.03 * 0.06, 0.5625 * 0.06),
    (0.7 * 0.06, 0.03 * 0.06),
    (0.7 * 0.06, 0.5625 * 0.06)
]
cut_cylinder1 = cq.Workplane("XY")
for x, y in cut_locations:
    cut_cylinder1 = cut_cylinder1.moveTo(x, y).circle(cut_radius).extrude(-cut_depth)
cut_cylinder2 = cq.Workplane("XY")
for x, y in cut_locations:
# Export
# 定义结果变量
result = cut_cylinder2
# 导出为STL文件
cq.exporters.export(result, "output_2436.stl