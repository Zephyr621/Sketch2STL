import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0021
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Rectangular Block (Cutout) ---
part_2_length = 0.375 * 0.375  # Scaled length
part_2_width = 0.375 * 0.375  # Scaled width
part_2_height = 0.0021
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1875, 0.1875, part_1_height))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(part_2)
# Export
# 导出为STL文件
cq.exporters.export(result, "output_2071.stl