import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.1289 * 0.75), (0.75 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.1406 * 0.75)
    .lineTo(0.625 * 0.75, 0.1406 * 0.75)
    .lineTo(0.625 * 0.75, 0.2478 * 0.75)
    .threePointArc((0.5997 * 0.75, 0.2277 * 0.75), (0.2785 * 0.75, 0.2478 * 0.75))
    .lineTo(0.2785 * 0.75, 0.2577 * 0.75)
    .lineTo(0.125 * 0.75, 0.2577 * 0.75)
    .lineTo(0.125 * 0.75, 0.2478 * 0.75)
    .lineTo(0.0, 0.2478 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_174.stl