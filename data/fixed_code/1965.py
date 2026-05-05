import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.4686 * 0.4686  # Scaled length
part_1_width = 0.1562 * 0.4686   # Scaled width
part_1_height = 0.0234
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Smaller Rectangular Prism on Top ---
part_2_length = 0.3871 * 0.3871  # Scaled length
part_2_width = 0.0158 * 0.3871   # Scaled width
part_2_height = 0.0129
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1965.stl