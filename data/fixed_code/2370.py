import cadquery as cq
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.0176 * 0.0361  # Sketch radius scaled
part_1_inner_radius = 0.0078 * 0.0361
part_1_height = 0.0652
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.3464, 0.3464, 0.0077))
# --- Part 2: Ring ---
part_2_outer_radius = 0.0126 * 0.0361  # Sketch radius scaled
part_2_inner_radius = 0.0078 * 0.0361
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height))
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2370.stl