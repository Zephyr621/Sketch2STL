import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.1888 * 0.75)
    .lineTo(0.5561 * 0.75, 0.1888 * 0.75)
    .lineTo(0.5561 * 0.75, 0.3106 * 0.75)
    .lineTo(0.75 * 0.75, 0.3106 * 0.75)
    .lineTo(0.75 * 0.75, 0.2574 * 0.75)
    .lineTo(0.6131 * 0.75, 0.2574 * 0.75)
    .lineTo(0.6131 * 0.75, 0.3346 * 0.75)
    .lineTo(0.5417 * 0.75, 0.3346 * 0.75)
    .lineTo(0.5417 * 0.75, 0.0)
    .lineTo(0.75 * 0.75,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_400.stl