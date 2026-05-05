import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.3571 * 0.3571  # Scaled length
part_1_width = 0.2857 * 0.3571  # Scaled width
part_1_height = 0.0982
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Rectangular Block ---
part_2_length = 0.2932 * 0.2932  # Scaled length
part_2_width = 0.1429 * 0.2932  # Scaled width
part_2_height = 0.1154
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1331.stl