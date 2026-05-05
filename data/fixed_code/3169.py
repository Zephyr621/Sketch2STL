import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.0346 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0058
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0058, 0))
# --- Part 2: Cutout ---
part_2_length = 0.0296 * 0.0296
part_2_width = 0.0199 * 0.0296
part_2_height = 0.0058
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3169.stl