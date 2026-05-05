import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.2547 * 0.75), (0.5 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.2188 * 0.75), (0.5 * 0.75, 0.4773 * 0.75))
    .lineTo(0.0, 0.4773 * 0.75)
    .threePointArc((0.0, 0.2188 * 0.75), (0.0, 0.0))
    .close()
    .moveTo(0.125 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.2547 * 0.75), (0.5 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.2277 * 0.75), (0.125 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3156.stl