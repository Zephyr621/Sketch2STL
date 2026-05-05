import cadquery as cq
# --- Part 1 ---
part_1_length = 0.75 * 0.75
part_1_width = 0.4635 * 0.75
part_1_height = 0.0116
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0458, 0))
# --- Part 2 ---
part_2_length = 0.6346 * 0.6346
part_2_width = 0.6346 * 0.6346
part_2_height = 0.0458
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0.3173 * 0.6346)
    .lineTo(0.6346 * 0.6346, 0.3173 * 0.6346)
    .lineTo(0.6346 * 0.6346, 0)
    .lineTo(0.4687 * 0.6346, 0)
    .lineTo(0.4687 * 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2110.stl