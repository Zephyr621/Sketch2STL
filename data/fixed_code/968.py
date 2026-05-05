import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0536 * 0.75)
    .lineTo(0.0536 * 0.75, 0.0)
    .lineTo(0.6667 * 0.75, 0.0)
    .lineTo(0.6667 * 0.75, 0.1091 * 0.75)
    .lineTo(0.5357 * 0.75, 0.1091 * 0.75)
    .lineTo(0.5357 * 0.75, 0.3889 * 0.75)
    .lineTo(0.3571 * 0.75, 0.3889 * 0.75)
    .lineTo(0.3571 * 0.75, 0.2143 * 0.75)
    .lineTo(0.1586 * 0.75, 0.2143 * 0.75)
    .lineTo(0.1586 * 0.75, 0.3214 * 0.75)
    .lineTo(0.0, 0.3214 * 0.75)
    .lineTo(0.0, 0.0536 * 0.75)
    .close()
    .extrude(0.04)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_968.stl