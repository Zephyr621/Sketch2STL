import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.4915 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.1875 + 0.1875  # Total extrusion depth
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.2477 * 0.6548  # Scaled length
part_2_width = 0.6548 * 0.6548  # Scaled width
part_2_height = 0.0864
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0597, 0.0597, 0.182))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_217.stl