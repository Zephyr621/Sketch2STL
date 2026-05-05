import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.6708 * 0.75, 0.0)
    .lineTo(0.6708 * 0.75, 0.75 * 0.75)
    .lineTo(0.4773 * 0.75, 0.75 * 0.75)
    .lineTo(0.4773 * 0.75, 0.2816 * 0.75)
    .lineTo(0.0, 0.2816 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4472)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_655.stl