import cadquery as cq
from math import radians
# --- Part 1: Ring ---
outer_radius = 0.1875 * 0.375  # Sketch radius scaled
inner_radius = 0.0938 * 0.375  # Inner radius scaled
height = 0.075
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.075, 0))
# --- Part 2: Ring ---
outer_radius_2 = 0.1875 * 0.375  # Sketch radius scaled
inner_radius_2 = 0.0938 * 0.375  # Inner radius scaled
height_2 = 0.075
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius_2)
    .extrude(height_2)
    .cut(cq.Workplane("XY").circle(inner_radius_2).extrude(height_2))
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3003.stl