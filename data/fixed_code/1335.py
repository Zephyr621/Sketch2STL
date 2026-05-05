import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.2536 * 0.75), (0.75 * 0.75, 0.5357 * 0.75))
    .threePointArc((0.375 * 0.75, 0.2143 * 0.75), (0.0, 0.0))
    .close()
    .extrude(0.1071)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1335.stl