import cadquery as cq
# --- Part 1: Rectangular Hollow Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4688 * 0.75  # Scaled width
part_1_height = 0.0938
inner_offset = 0.0112 * 0.75  # Scaled offset
outer_rect = cq.Workplane("XY").rect(part_1_length, part_1_width)
inner_rect = cq.Workplane("XY").rect(part_1_length - 2 * inner_offset, part_1_width - 2 * inner_offset).translate((0, 0.0113 * 0.75, 0))
part_1 = outer_rect.extrude(part_1_height).cut(inner_rect.extrude(part_1_height + 0.001))
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Cut Feature ---
part_2_length = 0.5625 * 0.5625  # Scaled length
part_2_width
# Export
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_2157.stl