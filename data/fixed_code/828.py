import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.4181 * 0.4181  # Scaled length
part_1_width = 0.1034 * 0.4181  # Scaled width
part_1_height = 0.0375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Prism (Join) ---
part_2_length = 0.0417 * 0.1286  # Scaled length
part_2_width = 0.1286 * 0.1286  # Scaled width
part_2_height = 0.0208
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_828.stl