import cadquery as cq
from math import radians
# --- Part 1: Ring ---
part_1_outer_radius = 0.2945 * 0.5893
part_1_inner_radius = 0.2595 * 0.5893
part_1_height = 0.1154 + 0.1154
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.1705 * 0.3357
part_2_inner_radius = 0.1154 * 0.3357
part_2_height = 0.0352 + 0.0352
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2192.stl