import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2893 * 0.75)
    .lineTo(0.5469 * 0.75, 0.4286 * 0.75)
    .lineTo(0.5611 * 0.75, 0.4286 * 0.75)
    .lineTo(0.2894 * 0.75, 0.4286 * 0.75)
    .lineTo(0.2894 * 0.75, 0.5729 * 0.75)
    .lineTo(0.0, 0.5729 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2386)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2386, 0))
# --- Assembly ---
assembly = part_1
cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1052.stl