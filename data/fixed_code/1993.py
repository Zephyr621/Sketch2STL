import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.75 * 0.75
part_1_width = 0.0157 * 0.75
part_1_height = 0.0071
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.7143 * 0.7143
part_2_width = 0.0414 * 0.7143
part_2_height = 0.2143
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1993.stl