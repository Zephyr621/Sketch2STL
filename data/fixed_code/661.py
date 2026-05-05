import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.2356 * 0.4712  # Sketch radius scaled
part_1_inner_radius = 0.125 * 0.4712  # Inner hole radius scaled
part_1_height = 0.1178
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0893, 0.1178, 0.0352))
# --- Part 2: Smaller Cylinder ---
part_2_radius = 0.0969 * 0.1924  # Sketch radius scaled
part_2_height = 0.4517
part_2 = (
    cq.Workplane("XY")
    .circle(part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_661.stl