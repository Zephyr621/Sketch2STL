import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Square Plate ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_thickness = 0.0625
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_thickness)
# --- Part 2: Holes ---
hole_radius = 0.0094 * 0.0312
hole_depth = 0.0281
hole_centers = [
    (0.0094 * 0.0312, 0.0094 * 0.0312),
    (0.0094 * 0.0312, 0.7395 * 0.0312),
    (0.7395 * 0.0312, 0.0094 * 0.0312),
    (0.7395 * 0.0312, 0.7395 * 0.0312)
]
part_2 = cq.Workplane("XY")
for x, y in hole_centers:
    part_2 = part_2.moveTo(x, y).circle(hole_radius)
part_2 = part_2.extrude(-hole_depth)
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1063.stl