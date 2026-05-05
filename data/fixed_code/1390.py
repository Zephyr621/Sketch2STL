import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hollow Center ---
part_1_outer_radius = 0.0816 * 0.163  # Sketch radius scaled
part_1_inner_radius = 0.0714 * 0.163  # Inner radius scaled
part_1_height = 0.225
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.0223 * 0.0469  # Sketch radius scaled
part_2_inner_radius = 0.0586 * 0.0469
part_2_height = 0.0357
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1390.stl