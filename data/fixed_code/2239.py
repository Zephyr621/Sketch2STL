import cadquery as cq
from math import radians
# --- Part 1: Cup Body ---
part_1_outer_radius = 0.3345 * 0.6729  # Sketch radius scaled
part_1_inner_radius = 0.3023 * 0.6729  # Inner radius scaled
part_1_height = 0.4821
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0375, 0.0375, 0))
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.0786 * 0.1458  # Sketch radius scaled
part_2_inner_radius = 0.3069 * 0.1458  # Inner radius scaled
part_2_height = 0.0188
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2239.stl