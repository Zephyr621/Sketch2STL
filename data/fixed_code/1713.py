import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.7083 * 0.7083  # Scaled length
part_1_width = 0.2833 * 0.7083   # Scaled width
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0341, 0.0268, 0.0))
# --- Part 2: Cylinders ---
cylinder_radius = 0.0099 * 0.0199  # Scaled radius
cylinder_height = 0.1251
cylinder1_x = 0.0099 * 0.0199
cylinder1_y = 0.0099 * 0.0199
cylinder2_x = 0.7083 * 0.0199
cylinder2_y = 0.0099 * 0.0199
cylinder3_x = 0.7083 * 0.0199
cylinder3_y = 0.0099 * 0.0199
cylinder4_x = 0.7083 * 0.0199
cylinder4_y = 0.0099 * 0.0199
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1713.stl