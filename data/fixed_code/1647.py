import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.2833 * 0.75  # Inner radius scaled
height = 0.3333
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(height)
)
# --- Part 2: Smaller Cylinder on Top ---
outer_radius_2 = 0.2833 * 0.75  # Sketch radius scaled
inner_radius_2 = 0.1483 * 0.75  # Inner radius scaled
height_2 = 0.1667
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius_2)
    .circle(inner_radius_2)
    .extrude(height_2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.3333))
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1483, 0.1483, 0.3333))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1647.stl