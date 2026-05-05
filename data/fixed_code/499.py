import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4687 * 0.75  # Scaled width
part_1_height = 0.0938
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Smaller Rectangular Section ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.4687 * 0.75  # Scaled width
part_2_height = 0.0938
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0, 0.4
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_499.stl