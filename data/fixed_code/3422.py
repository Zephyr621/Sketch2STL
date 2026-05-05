import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2753 * 0.75  # Scaled width
part_1_height = 0.1031
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1031, 0))
# --- Part 2: Cube Cutout ---
part_2_length = 0.4928 * 0.4928  # Scaled length
part_2_width = 0.2753 * 0.4928  # Scaled width
part_2_height = 0.1705
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extr
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3422.stl