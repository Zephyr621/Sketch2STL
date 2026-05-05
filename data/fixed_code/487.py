import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hollow Center ---
part_1_outer_radius = 0.3717 * 0.704  # Sketch radius scaled
part_1_inner_radius = 0.2935 * 0.704  # Inner radius scaled
part_1_height = 0.3088
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0134, 0.3088, 0.0134))
# --- Part 2: Smaller Cylinder on Top ---
part_2_outer_radius = 0.0268 * 0.0536  # Sketch radius scaled
part_2_inner_radius = 0.2935 * 0.0536  # Inner radius scaled
part_2_height = 0.1406
part_2 = (
    cq.Workplane("XY")
    .circle(part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_487.stl