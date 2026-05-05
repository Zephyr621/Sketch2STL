import cadquery as cq
# --- Part 1: Rectangular Object with Rounded Edges ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4688 * 0.75  # Scaled width
part_1_height = 0.0562
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_1_length, 0.0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0.15 * 0.75, part_1_width)
    .lineTo(0.15 * 0.75, 0.3438 * 0.75)
    .lineTo(0.3125 * 0.75, 0.3438 * 0.75)
    .lineTo(0.3125 * 0.75, 0.45 * 0.75)
    .lineTo(0.45 * 0.75, 0.45 * 0.75)
    .lineTo(0.45 * 0.75, part_1_width)
    .lineTo(0.15 * 0.75, part_1_width)
    .lineTo(0.0, part_1_width)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(part_1_height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2203.stl