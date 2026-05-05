import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.0536 * 0.75
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Small Cylinder on Top ---
part_2_radius = 0.0536 * 0.1023  # Sketch radius scaled
part_2_height = 0.0469
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.2331, 0.4687, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2047.stl