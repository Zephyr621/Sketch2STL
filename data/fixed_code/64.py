import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .threePointArc((0.3747 * 0.75, 0.2459 * 0.75), (0.75 * 0.75, 0.5 * 0.75))
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .threePointArc((0.3747 * 0.75, 0.3385 * 0.75), (0.375 * 0.75, 0.25 * 0.75))
    .lineTo(0.0, 0.25 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.03)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_64.stl