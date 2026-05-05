import cadquery as cq
# --- Part 1: Rectangular Bar ---
part_1_length = 0.0659 * 0.7679  # Scaled length
part_1_width = 0.7679 * 0.7679  # Scaled width
part_1_height = 0.0937
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0156, 0.0156, 0))
# --- Part 2: Rectangular Plate ---
part_2_length = 0.06697 * 0.7098  # Scaled length
part_2_width = 0.7098 * 0.7098  # Scaled width
part_2_height = 0.0169
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Assembly ---
assembly = part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_603.stl