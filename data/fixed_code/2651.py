import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.5 * 0.75, 0.25 * 0.75)
    .lineTo(0.5 * 0.75, 0.625 * 0.75)
    .lineTo(0.25 * 0.75, 0.625 * 0.75)
    .lineTo(0.25 * 0.75, 0.25 * 0.75)
    .lineTo(0, 0.25 * 0.75)
    .close()
    .extrude(0.25)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2651.stl