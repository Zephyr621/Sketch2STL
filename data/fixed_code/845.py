import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4102 * 0.75  # Scaled width
part_1_height = 0.0163
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.6328 * 0.6328  # Scaled length
part_2_width = 0.4324 * 0.6328  # Scaled width
part_2_height = 0.0312
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_845.stl