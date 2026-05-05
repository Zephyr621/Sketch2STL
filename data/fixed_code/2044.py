import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7484 * 0.75, 0.0)
    .threePointArc((0.7466 * 0.75, 0.2757 * 0.75), (0.75 * 0.75, 0.3621 * 0.75))
    .lineTo(0.75 * 0.75, 0.6896 * 0.75)
    .threePointArc((0.7466 * 0.75, 0.3577 * 0.75), (0.75 * 0.75, 0.6895 * 0.75))
    .lineTo(0.0, 0.6896 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0065)
)
# Cut out the first hole
hole1_center = (0.0314 * 0.75, 0.2952 * 0.75)
hole1 = (
    cq.Workplane("XY")
    .moveTo(hole1_center[0], hole1_center[1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2044.stl