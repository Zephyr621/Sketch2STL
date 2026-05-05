import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.0873 * 0.1771  # Scaled length
part_1_width = 0.1771 * 0.1771   # Scaled width
part_1_height = 0.1347
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0873, 0.1678, 0))
# --- Part 2: Rectangular Block (Cutout) ---
part_2_length = 0.0429 * 0.0714  # Scaled length
part_2_width = 0.0714 * 0.0714   # Scaled width
part_2_height = 0.0157
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1734.stl