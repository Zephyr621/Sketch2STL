import cadquery as cq
from math import radians
# --- Part 1: Circular Plate ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.175 * 0.75
part_1_height = 0.0969
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.025 * 0.05
part_2_inner_radius = 0.03 * 0.05
part_2_height = 0.375
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height))
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.3188, 0.3188, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_860.stl