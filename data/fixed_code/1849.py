import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate with Holes ---
part_1_length = 0.5769 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0346
hole_radius = 0.0544 * 0.75
hole_center_1 = (0.0793 * 0.75 - part_1_length/2, 0.0793 * 0.75 - part_1_width/2)
hole_center_2 = (0.5769 * 0.75 - part_1_length/2, 0.0793 * 0.75 - part_1_width/2)
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .pushPoints([hole_center_1, hole_center_2])
    .hole(2 * hole_radius)
)
# --- Part 2: Rectangular Bar ---
part_2_length = 0.5769 * 0.5696  # Scaled length
part_2_width = 0.5696 * 0.5696  # Scaled width
part_2_height = 0.1875
part_2 = (
    cq.Workplane("XY")
    .
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1849.stl