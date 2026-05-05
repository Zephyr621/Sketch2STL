import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.75 * 0.75
part_1_width = 0.6516 * 0.75
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Small Cube ---
part_2_length = 0.75 * 0.75
part_2_width = 0.3281 * 0.75
part_2_height = 0.0938
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3402.stl