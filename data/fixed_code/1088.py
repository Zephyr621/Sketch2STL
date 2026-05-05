import cadquery as cq
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.66 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.36
inner_length = (0.6 - 0.0737) * 0.75
inner_width = (0.7036 - 0.0769) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
part_1 = part_1.cut(cq.Workplane("XY").rect(inner_length, inner_width).translate((0.0737 * 0.75 - part_1_length/2 + inner_length/2, 0, part_1_height)))
# --- Part 2: Top Rectangular Box ---
part_2_length = 0.16 * 0.42  # Scaled length
part_2_width = 0.42 * 0.42  # Scaled width
part_2_height = 0.35
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1088.stl