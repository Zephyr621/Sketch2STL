import cadquery as cq
# --- Part 1: Base Rectangle ---
part_1_length = 0.25 * 0.5  # Scaled length
part_1_width = 0.5 * 0.5  # Scaled width
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Top Rectangle ---
part_2_length = 0.25 * 0.5  # Scaled length
part_2_width = 0.5 * 0.5  # Scaled width
part_2_height = 0.375
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(part_2_height)
)
# --- Assembly ---
# Translate parts to their final positions
part_1 = part_1.translate((0, 0, 0.375))
part_2 = part_2.translate((0, 0.375, 0.375))
assembly = part_1.union(part_2)
# --- Export to STL
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1408.stl