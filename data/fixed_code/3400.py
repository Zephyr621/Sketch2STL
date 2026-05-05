import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.5 * 0.75)
    .lineTo(0.0, 0.5 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.25)
)
# --- Part 2: Rectangular Box ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.5 * 0.75)
    .lineTo(
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3400.stl