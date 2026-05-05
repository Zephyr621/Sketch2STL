import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.3188
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3188, 0))
# --- Part 2: Ring ---
outer_radius = 0.2344 * 0.4688  # Outer radius scaled
inner_radius = 0.1875 * 0.4688  # Inner radius scaled
ring_height = 0.3188
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(ring_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0705, 0.3188, 0.0705
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3453.stl