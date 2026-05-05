import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.1304 * 0.75  # Scaled width
part_1_height = 0.0054
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: L-shaped Cutout ---
part_2_length = 0.7277 * 0.7277  # Scaled length
part_2_width = 0.1058 * 0.7277  # Scaled width
part_2_height = 0.1212
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3416.stl