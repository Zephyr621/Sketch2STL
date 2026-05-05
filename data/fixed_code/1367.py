import cadquery as cq
from math import radians
# --- Part 1: Ring ---
part_1_outer_radius = 0.1579 * 0.3099  # Sketch radius scaled
part_1_inner_radius = 0.1184 * 0.3099  # Inner radius scaled
part_1_height = 0.0307
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1473, 0.1473, 0.0171))
# --- Part 2: Cylinder with Hole ---
part_2_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_inner_radius = 0.1579 * 0.75  # Inner radius scaled
part_2_height = 0.0078
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1367.stl