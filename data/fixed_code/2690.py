import cadquery as cq
from math import radians
# --- Part 1: Ring ---
part_1_outer_radius = 0.2812 * 0.575  # Sketch radius scaled
part_1_inner_radius = 0.3125 * 0.575
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2589, 0))
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.2661 * 0.5759  # Sketch radius scaled
part_2_inner_radius = 0.1406 * 0.5759
part_2_height = 0.2589
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2690.stl