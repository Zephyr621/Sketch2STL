import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.15 * 0.3  # Sketch radius scaled
part_1_inner_radius = 0.075 * 0.3  # Inner hole radius scaled
part_1_height = 0.27
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.15, 0.27, 0.15))
# --- Part 2: Washer ---
part_2_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_inner_radius = 0.15 * 0.75  # Inner hole radius scaled
part_2_height = 0.0125
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2128.stl