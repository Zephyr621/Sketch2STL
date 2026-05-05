import cadquery as cq
# --- Part 1: Base Rectangle ---
part_1_length = 0.5625 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.5625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.1875 * 0.375  # Scaled length
part_2_width = 0.375 * 0.375   # Scaled width
part_2_height = 0.0312
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1793.stl