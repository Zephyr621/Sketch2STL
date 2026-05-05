import cadquery as cq
# --- Part 1: Cube with Cut Off ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6672 * 0.75  # Scaled width
part_1_height = 0.1299
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length / 2, part_1_width)
    .lineTo(0, 0)
    .close()
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: L-shaped CAD Model ---
part_2_length = 0.6643 * 0.6562  # Scaled length
part_2_width = 0.5385 * 0.6562  # Scaled width
part_2_height = 0.0477
part_2 = (
    cq.Workplane("XY")
    .moveTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3210.stl