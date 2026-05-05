import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1667)
    .threePointArc((0.7385, 0.1571), (0.6136, 0.33))
    .lineTo(0.2139, 0.33)
    .lineTo(0.0, 0.1667)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2139 * 0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3532.stl