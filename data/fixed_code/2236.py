import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5357 * 0.75  # Scaled width
part_1_height = 0.3214
inner_offset = 0.0107 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
part_1 = part_1.cut(cq.Workplane("XY").rect(part_1_length - 2 * inner_offset, part_1_width - 2 * inner_offset).translate((0, 0.0536 * 0.75 - 0.0107 * 0.75, 0)).extrude(part_1_height + 0.001))
# --- Part 2: Rectangular Plate (Cut) ---
part_2_length = 0.2143 * 0.5357  # Scaled length
part_2_width = 0.5357 * 0.5357  # Scaled width
part_2_height = 0.0214
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2236.stl