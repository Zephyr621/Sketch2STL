import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.625, 0.0)
    .lineTo(0.25 * 0.625, 0.125 * 0.625)
    .lineTo(0.5 * 0.625, 0.125 * 0.625)
    .lineTo(0.5 * 0.625, 0.0)
    .lineTo(0.625 * 0.625, 0.0)
    .lineTo(0.625 * 0.625, 0.625 * 0.625)
    .lineTo(0.0, 0.625 * 0.625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2502.stl