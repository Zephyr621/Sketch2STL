import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75
part_1_width = 0.6733 * 0.75
part_1_height = 0.0197
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0197, 0))
# --- Part 2: Square Box ---
part_2_length = 0.709 * 0.709
part_2_width = 0.6667 * 0.709
part_2_height = 0.017
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3537.stl