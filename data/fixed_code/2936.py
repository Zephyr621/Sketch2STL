import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.4095 * 0.4095  # Scaled length
part_1_width = 0.1382 * 0.4095  # Scaled width
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cut Feature ---
cut_length = 0.1382 * 0.1382  # Scaled length
cut_width = 0.0375 * 0.1382  # Scaled width
cut_height = 0.15
cut_1 = (
    cq.Workplane("XY")
    .rect(cut
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2936.stl