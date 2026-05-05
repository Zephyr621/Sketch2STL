import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3 * 0.75, 0.0)
    .lineTo(0.3 * 0.75, 0.225 * 0.75)
    .threePointArc((0.375 * 0.75, 0.225 * 0.75), (0.45 * 0.75, 0.225 * 0.75))
    .lineTo(0.45 * 0.75, 0.45 * 0.75)
    .lineTo(0.6 * 0.75, 0.45 * 0.75)
    .threePointArc((0.375 * 0.75, 0.225 * 0.75), (0.6 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.225 * 0.75)
    .lineTo(0.0, 0.225 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.15 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_566.stl