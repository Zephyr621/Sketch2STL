import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.7407 * 0.7407  # Scaled length
part_1_width = 0.0926 * 0.7407   # Scaled width
part_1_height = 0.0926
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0038, 0.0038, 0.0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.0375 * 0.0375  # Scaled length
part_2_width = 0.0125 * 0.0375   # Scaled width
part_2_height = 0.15
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.00
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1878.stl