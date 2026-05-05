import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.7281 * 0.7281  # Scaled length
part_1_width = 0.1753 * 0.7281   # Scaled width
part_1_height = 0.0105
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0105, 0.0224, 0))
# --- Part 2: Rectangular Box ---
part_2_length = 0.7282 * 0.7282  # Scaled length
part_2_width = 0.1753 * 0.7282   # Scaled width
part_2_height = 0.75
inner_offset = 0.0058 * 0.7282
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
inner_box = (
    cq.Workplane("XY")
    .rect(part_2_length - 2 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2751.stl