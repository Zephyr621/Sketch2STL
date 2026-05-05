import cadquery as cq
from math import radians
# --- Part 1: Circular Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.2109 * 0.75  # Inner hole radius scaled
height = 0.0188
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0469, 0.0038, 0.0038))
# --- Part 2: Cylinder with Hole ---
outer_radius_2 = 0.0094 * 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3021.stl