import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.225)
    .lineTo(0.525, 0.225)
    .threePointArc((0.375, 0.15), (0.15, 0.225))
    .lineTo(0.0, 0.225)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3 * 0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2096.stl