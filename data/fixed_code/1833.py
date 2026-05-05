import cadquery as cq
from math import radians
# --- Part 1: Base ---
part_1_width = 0.3659 * 0.75
part_1_length = 0.75 * 0.75
part_1_height = 0.4537
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusions ---
part_2_radius = 0.0161 * 0.5598
part_2_height = 0.075
part_2 = (
    cq.Workplane("XY")
    .pushPoints([(0.0161 * 0.5598 - part_1_width/2, 0.0161 * 0.5598 - part_1_length/2)])
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1833.stl