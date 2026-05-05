import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5833 * 0.75  # Scaled width
part_1_height = 0.0174
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Block (Cutout) ---
part_2_length = 0.1793 * 0.1793  # Scaled length
part_2_width = 0.1793 * 0.1793  # Scaled width
part_2_height = 0.0099
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_114.stl