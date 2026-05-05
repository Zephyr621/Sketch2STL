import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.5167 * 0.75, 0.0)
    .lineTo(0.5167 * 0.75, 0.2143 * 0.75)
    .lineTo(0.5833 * 0.75, 0.2143 * 0.75)
    .lineTo(0.5833 * 0.75, 0.4286 * 0.75)
    .lineTo(0.2308 * 0.75, 0.4286 * 0.75)
    .lineTo(0.2308 * 0.75, 0.2957 * 0.75)
    .lineTo(0.0, 0.2957 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0017)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1167.stl