import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0214 * 0.75  # Scaled width
part_1_height = 0.2143
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2143))
# --- Part 2: Rectangular Cutout ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.0214 * 0.75  # Scaled width
part_2_height = 0.3214
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1561.stl