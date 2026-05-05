import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.0156 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0156
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cube (Cutout) ---
part_2_size = 0.0156 * 0.0156  # Scaled size
part_2_depth = 0.0312
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0078, 0.0078, part_1_height))
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2565.stl