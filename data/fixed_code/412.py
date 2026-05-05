import cadquery as cq
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.2953 * 0.75
part_1_height = 0.1254
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Rectangular Prism ---
part_2_width = 0.2709 * 0.2709  # Sketch width scaled
part_2_length = 0.2709 * 0.2709  # Sketch length scaled
part_2_height = 0.1653
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_length)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1364, 0.2308, 0.1254))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_412.stl