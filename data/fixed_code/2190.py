import cadquery as cq
from cadquery import exporters
# --- Part 1: Ring ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3281 * 0.75
part_1_height = 0.0652
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0652, 0))
# --- Part 2: Cylinder with Hole ---
part_2_outer_radius = 0.325 * 0.6562  # Sketch radius scaled
part_2_inner_radius = 0.3281 * 0.6562
part_2_height = 0.4286
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction for a hole
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2190.stl