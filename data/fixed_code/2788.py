import cadquery as cq
# --- Part 1: Square Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6915 * 0.75  # Scaled width
part_1_height = 0.0069
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0069))
# --- Part 2: Rectangular Object ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.6915 * 0.75  # Scaled width
part_2_height = 0.0069
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_1.union(part_2)
cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2788.stl