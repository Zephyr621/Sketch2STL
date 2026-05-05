import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.3276 * 0.3276  # Scaled length
part_1_width = 0.1211 * 0.3276  # Scaled width
part_1_height = 0.0014
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.4347, 0.0118, 0))
# --- Part 2: Rectangular Plate (Cutout) ---
part_2_length = 0.3276 * 0.3276  # Scaled length
part_2_width = 0.1211 * 0.3276  # Scaled width
part_2_height = 0.0014
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3155.stl