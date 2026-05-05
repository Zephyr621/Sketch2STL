import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4412 * 0.4412  # Scaled length
part_1_width = 0.2143 * 0.4412  # Scaled width
part_1_height = 0.0087
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1786, 0.1607, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.2143 * 0.75  # Scaled width
part_2_height = 0.0056
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3352.stl