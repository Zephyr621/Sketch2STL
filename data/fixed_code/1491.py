import cadquery as cq
from math import radians
# --- Part 1: Cup ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3281 * 0.75
part_1_height = 0.0225
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0225, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.2767 * 0.5  # Sketch radius scaled
part_2_height = 0.0125
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1491.stl