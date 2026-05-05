import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4286 * 0.75  # Scaled width
part_1_height = 0.0049
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Holes ---
hole_radius = 0.0032 * 0.7096  # Scaled radius
hole_depth = 1.05
# Hole positions (scaled and translated)
hole_positions = [
    (-0.0032 * 0.7096, -0.0032 * 0.7096),  # Bottom Left
    (0.0032 * 0.7096, -0.1608 * 0.7096),  # Top Left
    (0.4828 * 0.7096, -0.0032 * 0.7096),  # Bottom Right
    (0.4828 * 0.7096, -0.1608 * 0.7096)   # Top Right
]
# Create holes by cutting cylinders
for x, y in hole_positions:
    hole = cq.Workplane("XY").circle(hole_radius).extrude(-hole_depth)
# 定义结果变量
result = hole
# 导出为STL文件
cq.exporters.export(result, "output_3530.stl