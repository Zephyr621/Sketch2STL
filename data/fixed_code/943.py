import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.1682 * 0.1808  # Scaled length
part_1_width = 0.1808 * 0.1808  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Part 2: Rectangular Cutout ---
part_2_length = 0.0117 * 0.0352  # Scaled length
part_2_width = 0.0352 * 0.0352  # Scaled width
part_2_height = 0.0507
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Assembly: Apply Translation and Cut ---
assembly = part_1.cut(part_2.translate((0.0041,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_943.stl