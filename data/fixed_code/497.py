import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0312)
    .threePointArc((0.375, 0.0313), (0.0, 0.0625))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0196 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0196 * 0.75, 0))
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
cq.exporters.export(result, "output_497.stl