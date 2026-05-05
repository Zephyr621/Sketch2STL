import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.63 * 0.63  # Scaled length
part_1_width = 0.36 * 0.63  # Scaled width
part_1_height = 0.03
inner_rect_offset = 0.0188 * 0.63
inner_rect_size = (0.2 - 0.0188) * 0.63
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_rect_size, inner_rect_size)
    .extrude(part_1_height + 0.1)  # Extrude slightly more to ensure complete cut
)
part_1 = part_1.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0188, 0.0188, 0))
# --- Part 2: Cut Feature ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.34 * 0.75  # Scaled width
part_2_height = 0.09
part_2 =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1585.stl