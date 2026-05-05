import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.2812 * 0.5625  # Sketch radius scaled
part_1_inner_radius = 0.1406 * 0.5625  # Inner hole radius scaled
part_1_height = 0.0938 + 0.0938
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Cut Feature ---
part_2_radius = 0.1875 * 0.375  # Sketch radius scaled
part_2_depth = 0.075 + 0.075
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3041.stl