import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4687 * 0.75  # Scaled width
part_1_height = 0.2391
inner_rect_x = 0.3488 * 0.75
inner_rect_y = 0.4688 * 0.75
inner_rect_size = (0.5625 - 0.3488) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_rect_size, inner_rect_size)
    .extrude(part_1_height + 0.001)  # Extrude slightly more to ensure complete cut
)
part_1 = part_1.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2391, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2314.stl