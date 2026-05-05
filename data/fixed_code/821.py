import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.5417 * 0.5377  # Sketch length scaled
part_1_width = 0.5377 * 0.5377  # Sketch width scaled
part_1_height = 0.4821
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0811, 0.4821, 0))
# --- Part 2: Rectangular Box ---
part_2_length = 0.4853 * 0.4873  # Sketch length scaled
part_2_width = 0.4873 * 0.4873  # Sketch width scaled
part_2_height = 0.2083
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.4821, 0.0811))
# --- Assembly ---
assembly = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_821.stl