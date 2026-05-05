import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.1875 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.002
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# Coordinate System Transformation for Part 1
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cylinder ---
part_2_radius = 0.2812 * 0.5625
part_2_height = 0.1875
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3036.stl