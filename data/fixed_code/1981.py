import cadquery as cq
# --- Part 1: Triangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6495 * 0.75  # Scaled width
part_1_height = 0.1581
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Cutout ---
part_2_length = 0.2709 * 0.2709  # Scaled length
part_2_width = 0.2493 * 0.2709  # Scaled width
part_2_height = 0.1821
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1981.stl