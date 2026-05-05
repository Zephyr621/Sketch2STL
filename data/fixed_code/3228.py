import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3746 * 0.75, 0.0)
    .threePointArc((0.7467 * 0.75, 0.1789 * 0.75), (0.7125 * 0.75, 0.4773 * 0.75))
    .lineTo(0.75 * 0.75, 0.4773 * 0.75)
    .threePointArc((0.7467 * 0.75, 0.3883 * 0.75), (0.7125 * 0.75, 0.4773 * 0.75))
    .lineTo(0.0, 0.4773 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1296)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.exp
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3228.stl