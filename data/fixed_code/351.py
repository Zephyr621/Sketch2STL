import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.75, 0.0)
    .lineTo(0.25 * 0.75, 0.0188 * 0.75)
    .lineTo(0.5 * 0.75, 0.0188 * 0.75)
    .lineTo(0.5 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1774 * 0.75)
    .lineTo(0.375 * 0.75, 0.1774 * 0.75)
    .lineTo(0.0, 0.1774 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0313)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_351.stl