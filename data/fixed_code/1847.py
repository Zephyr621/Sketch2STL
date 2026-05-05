import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.73 * 0.73  # Scaled length
part_1_width = 0.35 * 0.73   # Scaled width
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.075, 0))
# --- Part 2: Smaller Rectangular Section ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.15 * 0.75   # Scaled width
part_2_height = 0.0225
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1847.stl