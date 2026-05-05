import cadquery as cq
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.1219 * 0.623  # Sketch radius scaled
part_1_inner_radius = 0.0578 * 0.623  # Sketch radius scaled
part_1_height = 0.1875 + 0.1875
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Ring ---
part_2_outer_radius = 0.0769 * 0.1452  # Sketch radius scaled
part_2_inner_radius = 0.0578 * 0.1452  # Sketch radius scaled
part_2_height = 0.0393 + 0.0393
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1977.stl