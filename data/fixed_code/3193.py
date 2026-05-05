import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2357 * 0.75  # Scaled width
part_1_height = 0.0521
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cube ---
part_2_size = 0.125 * 0.125  # Scaled size
part_2_height = 0.0148
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Part 3: Cube (Join Operation) ---
part_3_size = 0.25 * 0.25  # Scaled size
part_3_height = 0.0148
part_3 =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3193.stl