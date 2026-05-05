import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7484 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.2709 * 0.75), (0.75 * 0.75, 0.5455 * 0.75))
    .lineTo(0.0, 0.5455 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2517)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2349.stl