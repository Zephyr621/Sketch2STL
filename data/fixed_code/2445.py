import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.225 * 0.75)
    .lineTo(0.525 * 0.75, 0.225 * 0.75)
    .lineTo(0.525 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.45 * 0.75)
    .lineTo(0.525 * 0.75, 0.45 * 0.75)
    .lineTo(0.525 * 0.75, 0.45 * 0.75)
    .lineTo(0.25 * 0.75, 0.45 * 0.75)
    .lineTo(0.25 * 0.75, 0.225 * 0.75)
    .lineTo(0.0, 0.225 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.15)
)
# ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2445.stl