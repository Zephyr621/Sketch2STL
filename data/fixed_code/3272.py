import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hollow Center ---
part_1_outer_radius = 0.1446 * 0.2893  # Sketch radius scaled
part_1_inner_radius = 0.0749 * 0.2893  # Inner radius scaled
part_1_height = 0.2536
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0156, 0, 0))
# --- Part 2: Curved Top ---
part_2_scale = 0.1948
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.0939 * part_2_scale, 0.0939 * part_2_scale), (0.1948 * part_2_scale, 0.0))
    .lineTo(0.1948 * part_2_scale, 0.0939 * part_2_scale)
    .threePointArc((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3272.stl