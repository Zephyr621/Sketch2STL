import cadquery as cq
# --- Part 1: Base with Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0398 * 0.75, 0.0)
    .lineTo(0.0398 * 0.75, 0.2982 * 0.75)
    .lineTo(0.7125 * 0.75, 0.2982 * 0.75)
    .lineTo(0.7125 * 0.75, 0.0361 * 0.75)
    .lineTo(0.75 * 0.75, 0.0361 * 0.75)
    .lineTo(0.75 * 0.75, 0.3343 * 0.75)
    .lineTo(0.0, 0.3343 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1355)
)
# Add the cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(0.0398 * 0.75, 0.0361 * 0.75)
    .lineTo(0.0398 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_552.stl