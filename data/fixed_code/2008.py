import cadquery as cq
# --- Part 1: Ring ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3388 * 0.75
part_1_height = 0.11412
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Rectangular Prism with Circular Hole ---
part_2_length = 0.4688 * 0.4688  # Sketch length scaled
part_2_width = 0.6328 * 0.4688  # Sketch width scaled
part_2_height = 0.0393
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0094, 0.0094, 0.11412))
# --- Assembly ---
assembly = part_1.union(part_2)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2008.stl