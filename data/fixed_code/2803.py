import cadquery as cq
# --- Part 1: Base Rectangular Block ---
part_1_length = 0.75 * 0.75
part_1_width = 0.6635 * 0.75
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.0194 * 0.0375
part_2_width = 0.0375 * 0.0375
part_2_height = 0.0375
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2803.stl