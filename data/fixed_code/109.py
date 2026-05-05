import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.2344 * 0.4688  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.75, 0, 0))
# --- Part 2: Cutout ---
part_2_outer_radius = 0.1172 * 0.2344  # Sketch radius scaled
part_2_inner_radius = 0.1172 * 0.2344
part_2_depth = 0.1172
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 180)
part_2 = part_2.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_109.stl