import cadquery as cq
# --- Part 1: T-shaped Object ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.625 * 0.75)
    .lineTo(0.5 * 0.75, 0.625 * 0.75)
    .lineTo(0.5 * 0.75, 0.2746 * 0.75)
    .lineTo(0.25 * 0.75, 0.2746 * 0.75)
    .lineTo(0.25 * 0.75, 0.0625 * 0.75)
    .lineTo(0.0, 0.0625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.25 * 0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# --- Export to STL ---
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2472.stl