import cadquery as cq
from math import radians
# --- Part 1: Circular Plate ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.2297 * 0.75
part_1_height = 0.0281
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Hole ---
part_2_radius = 0.2297 * 0.4594  # Sketch radius scaled
part_2_depth = 0.0156
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.0281)
    .moveTo(0.1969, 0.1969)
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1450.stl