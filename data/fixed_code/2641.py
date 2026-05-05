import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.5 * 0.5  # Scaled length
part_1_width = 0.25 * 0.5   # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Top Protrusion ---
part_2_length = 0.25 * 0.25  # Scaled length
part_2_width = 0.25 * 0.25   # Scaled width
part_2_height = 0.625
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0.125 * 0.25, part_2_width)
    .lineTo(0.125 * 0.25, part_2_width)
    .lineTo(0.0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2641.stl