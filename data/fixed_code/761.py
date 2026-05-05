import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0645 * 0.735  # Sketch radius scaled
part_1_height = 0.7
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0082, 0.75, 0.0082))
# --- Part 2: L-Shaped Cutout ---
sketch_scale = 0.75
extrude_depth = 0.1875 + 0.1875
# Define points for the sketch
points = [
    (0.0, 0.0187),
    (0.0187, 0.0187),
    (0.7, 0.0187),
    (0.7, 0.1225),
    (0.0187, 0.1225),
    (0.0187, 0.0),
]
# Scale the points
scaled_points = [(x * sketch_scale, y * sketch_scale) for x, y in points]
# Create the L shape using the scaled points
part_2 = cq.Workplane("XY")
for
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_761.stl