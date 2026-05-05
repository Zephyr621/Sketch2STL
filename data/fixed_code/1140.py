import cadquery as cq
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Part 2: Cutout 1 ---
part_2_length = 0.25 * 0.375  # Scaled length
part_2_width = 0.375 * 0.375  # Scaled width
part_2_height = 0.125
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1140.stl