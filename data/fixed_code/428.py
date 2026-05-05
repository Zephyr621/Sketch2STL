import cadquery as cq
# --- Part 1: Rectangular Protrusion ---
part_1_length = 0.0343 * 0.0343  # Scaled length
part_1_width = 0.0129 * 0.0343  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.0282 * 0.0282  # Scaled length
part_2_width = 0.0129 * 0.0282  # Scaled width
part_2_height = 0.7496
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_428.stl