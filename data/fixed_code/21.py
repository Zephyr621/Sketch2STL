import cadquery as cq
# --- Part 1: Base Rectangle ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4495 * 0.75  # Scaled width
part_1_height = 0.4286
cutout_x_start = 0.1667 * 0.75
cutout_y_start = 0.2411 * 0.75
cutout_size = (0.4971 - 0.1667) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
cutout = (
    cq.Workplane("XY")
    .rect(cutout_size, cutout_size)
    .extrude(part_1_height + 0.1)  # Extrude slightly more to ensure complete cut
    .translate((cutout_x_start - part_1_length / 2, cutout_y_start - part_1_width / 2, 0))
)
part_1 = part_1.cut(cutout)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_21.stl