import cadquery as cq
# --- Part 1: Square Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.675 * 0.75  # Scaled width
part_1_height = 0.2025
inner_offset = 0.0375 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").rect(part_1_length - 2 * inner_offset, part_1_width - 2 * inner_offset).extrude(part_1_height + 0.1))
)
# --- Part 2: Cube with Rounded Edges ---
part_2_size = 0.6 * 0.675  # Scaled size
part_2_height = 0.2
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.075, 0.075, 0.2025))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_669.stl