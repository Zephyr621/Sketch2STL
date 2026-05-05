import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.4375 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.125
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# Create holes in Part 1
hole_radius = 0.0312 * 0.75
hole_centers = [
    (0.0938 * 0.75 - part_1_length/2, 0.0938 * 0.75 - part_1_width/2),
    (0.2812 * 0.75 - part_1_length/2, 0.0938 * 0.75 - part_1_width/2),
    (0.2755 * 0.75 - part_1_length/2, 0.0938 * 0.75 - part_1_width/2),
    (0.2755 * 0.75 - part_1_length/2, 0.6562 * 0.75 - part_1_width/2),
]
for center_x, center_y in hole_centers:
    part_1 = part_1
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2263.stl