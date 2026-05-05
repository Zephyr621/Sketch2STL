import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.625 * 0.75  # Sketch width scaled
part_1_height = 0.0625 + 0.0625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Box (Cutout) ---
part_2_length = 0.1875 * 0.375  # Sketch length scaled
part_2_width = 0.375 * 0.375  # Sketch width scaled
part_2_height = 0.125 + 0.125
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0.375 * 0.375)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, 0.375 * 0.375)
    .close()
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.5625, 0, 0))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3535.stl