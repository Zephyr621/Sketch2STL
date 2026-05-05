import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0117 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.0273 * 0.75), (0.4911 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1254 * 0.75)
    .threePointArc((0.375 * 0.75, 0.2209 * 0.75), (0.2469 * 0.75, 0.4496 * 0.75))
    .lineTo(0.0, 0.1254 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0125)
)
# --- Assembly ---
assembly = part_1
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1475.stl