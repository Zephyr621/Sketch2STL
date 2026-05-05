import cadquery as cq
# --- Part 1: Washer ---
part_1_length = 0.2625 * 0.7262  # Scaled length
part_1_width = 0.7262 * 0.7262   # Scaled width
part_1_height = 0.0891
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0188, 0.0188, 0))
# --- Part 2: Cutout ---
part_2_length = 0.1475 * 0.1475  # Scaled length
part_2_width = 0.1568 * 0.1475   # Scaled width
part_2_height = 0.0375
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3394.stl