import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.1875 * 0.375  # Sketch radius scaled
inner_radius = 0.125 * 0.375  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Hole ---
hole_radius = 0.0937 * 0.1875  # Sketch radius scaled
hole_depth = 0.5625
part_2 = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(-hole_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_248.stl