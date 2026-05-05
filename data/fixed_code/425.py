import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.1875 * 0.75)
    .lineTo(0.5625 * 0.75, 0.1875 * 0.75)
    .lineTo(0.5625 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.5625 * 0.75)
    .lineTo(0.5625 * 0.75, 0.5625 * 0.75)
    .lineTo(0.1875 * 0.75, 0.5625 * 0.75)
    .lineTo(0.1875 * 0.75, 0.1875 * 0.75)
    .lineTo(0.0, 0.1875 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_425.stl