import cadquery as cq
# --- Part 1: Ring ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3214 * 0.75
part_1_height = 0.0931
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.3214 * 0.6429  # Sketch radius scaled
part_2_inner_radius = 0.2586 * 0.6429
part_2_height = 0.6562
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_187.stl