import cadquery as cq
from math import radians
# --- Part 1: Circular Plate ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.25 * 0.75
part_1_height = 0.0281
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Washer ---
part_2_outer_radius = 0.25 * 0.5  # Sketch radius scaled
part_2_inner_radius = 0.2188 * 0.5
part_2_height = 0.2812
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height))
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2424.stl