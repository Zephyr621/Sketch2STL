import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.25 * 0.25  # Scaled length
part_1_width = 0.25 * 0.25  # Scaled width
part_1_height = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Part 2: Cube ---
part_2_length = 0.125 * 0.25  # Scaled length
part_2_width = 0.25 * 0.25  # Scaled width
part_2_height = 0.25
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2091.stl