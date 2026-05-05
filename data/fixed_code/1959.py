import cadquery as cq
# --- Part 1: Base Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.25 * 0.25  # Scaled length
part_2_width = 0.25 * 0.25  # Scaled width
part_2_height = 0.125
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(0.25 * 0.25, part_2_width)
    .lineTo(0.0, part_2_width)
    .close()
    .extrude(-part_2_height)
)
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2.translate((0.25, 0.0, part_1_height)))
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1959.stl