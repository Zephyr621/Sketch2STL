import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0703
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cylinders ---
cylinder_radius = 0.0937 * 0.1875  # Scaled radius
cylinder_height = 0.0937
cylinder_centers = [
    (0.0938 * 0.1875, 0.0938 * 0.1875),
    (0.0938 * 0.1875, 0.5625 * 0.1875),
    (0.2812 * 0.1875, 0.0938 * 0.1875),
]
part_2 = cq.Workplane("XY")
for x, y in cylinder_centers
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_286.stl