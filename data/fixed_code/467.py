import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.75, 0.0)
    .lineTo(0.25 * 0.75, 0.75 * 0.75)
    .lineTo(0.5 * 0.75, 0.75 * 0.75)
    .lineTo(0.5 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.5 * 0.75)
    .lineTo(0.0, 0.5 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.exp
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_467.stl