import cadquery as cq
from math import radians
# --- Part 1: Circular Plate ---
part_1_outer_radius = 0.375 * 0.75
part_1_inner_radius = 0.3309 * 0.75
part_1_height = 0.0281
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Cylinder ---
part_2_radius = 0.3309 * 0.675
part_2_inner_radius = 0.1667 * 0.675
part_2_height = 0.4688
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height))
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2235.stl