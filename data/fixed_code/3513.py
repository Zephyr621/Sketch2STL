import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.3791 * 0.5687  # Scaled length
part_1_width = 0.5687 * 0.5687  # Scaled width
part_1_height = 0.0117
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Box ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.5687 * 0.75  # Scaled width
part_2_height = 0.0234
inner_offset = 0.0083 * 0.75
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
inner_box = (
    cq.Workplane("XY")
    .rect(part_2_length - 2 * inner_offset, part_2_width - 2 * inner_offset)
    .extrude(part_2_height + 0.001)  # Extrude slightly more to
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3513.stl