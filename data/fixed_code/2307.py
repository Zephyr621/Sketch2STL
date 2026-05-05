import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.5568 * 0.5568  # Scaled length
part_1_width = 0.3621 * 0.5568   # Scaled width
part_1_height = 0.2945
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0515, 0.0216, 0))
# --- Part 2: Smaller Cube ---
part_2_length = 0.5568 * 0.5568  # Scaled length
part_2_width = 0.3621 * 0.5568   # Scaled width
part_2_height = 0.2945
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2307.stl