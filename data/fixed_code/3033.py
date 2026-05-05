import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0357 * 0.75  # Scaled width
part_1_height = 0.0108
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Part 2: Cutout ---
part_2_length = 0.5357 * 0.5357  # Scaled length
part_2_width = 0.0536 * 0.5357  # Scaled width
part_2_height = 0.0108
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3033.stl