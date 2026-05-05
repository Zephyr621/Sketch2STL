import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2728 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2728 * 0.75)
    .lineTo(0.5357 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2679 * 0.75)
    .lineTo(0.2571 * 0.75, 0.2679 * 0.75)
    .lineTo(0.2571 * 0.75, 0.2728 * 0.75)
    .lineTo(0.0, 0.2728 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0288)
)
# --- Assembly ---
assembly = part_1
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2928.stl