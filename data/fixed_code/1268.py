import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.6632 * 0.6632  # Scaled length
part_1_width = 0.4091 * 0.6632  # Scaled width
part_1_height = 0.0179
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0293, 0.0293, 0))
# --- Part 2: Rectangular Block (Cutout) ---
part_2_length = 0.7187 * 0.7187  # Scaled length
part_2_width = 0.4091 * 0.7187  # Scaled width
part_2_height = 0.0083
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1268.stl