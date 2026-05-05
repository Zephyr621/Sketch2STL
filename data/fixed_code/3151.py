import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.125
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Part 2: Rectangular Block ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.375 * 0.75  # Scaled width
part_2_height = 0.125
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Part 3: Rectangular Block ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3151.stl