import cadquery as cq
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.2344 * 0.4688  # Sketch radius scaled
part_1_inner_radius = 0.125 * 0.4688   # Sketch radius scaled
part_1_height = 0.1016
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Ring ---
part_2_outer_radius = 0.2188 * 0.4375  # Sketch radius scaled
part_2_inner_radius = 0.125 * 0.4375   # Sketch radius scaled
part_2_height = 0.0312
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2057.stl