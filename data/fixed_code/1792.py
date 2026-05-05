import cadquery as cq
from math import radians
# --- Part 1: Ring ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3024 * 0.75
part_1_height = 0.1416
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1416, 0))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.0865 * 0.1611  # Sketch radius scaled
part_2_height = 0.0205
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1792.stl