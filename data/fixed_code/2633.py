import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.25 * 0.25  # Scaled length
part_1_width = 0.125 * 0.25  # Scaled width
part_1_height = 0.125
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.5, 0))
# --- Part 2: L-shaped CAD Model ---
part_2_length = 0.375 * 0.375  # Scaled length
part_2_width = 0.125 * 0.375  # Scaled width
part_2_height = 0.625
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2633.stl