import cadquery as cq
from math import radians
# --- Part 1: Ring Base ---
part_1_outer_radius = 0.2308 * 0.4767  # Sketch radius scaled
part_1_inner_radius = 0.125 * 0.4767  # Inner radius scaled
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Part 2: Ring Top ---
part_2_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_inner_radius = 0.2297 * 0.75  # Inner radius scaled
part_2_height = 0.25
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_214.stl