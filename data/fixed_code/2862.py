import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2903 * 0.75  # Scaled width
part_1_height = 0.2903
inner_offset = 0.0104 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .rect(part_1_length - 2 * inner_offset, part_1_width - 2 * inner_offset)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2903))
# --- Part 2: Rectangular Block ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.2903 * 0.75  # Scaled width
part_2_height = 0.2903
inner_offset_x = 0.375 * 0.75
inner_offset_y = 0.1289 * 0.75
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2862.stl