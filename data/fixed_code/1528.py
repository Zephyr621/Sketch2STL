import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.4286 * 0.75)
    .lineTo(0.1608 * 0.75, 0.4286 * 0.75)
    .threePointArc((0.2143 * 0.75, 0.2083 * 0.75), (0.3214 * 0.75, 0.0))
    .lineTo(0.3214 * 0.75, 0.5357 * 0.75)
    .lineTo(0.6429 * 0.75, 0.5357 * 0.75)
    .threePointArc((0.6429 * 0.75, 0.5625 * 0.75), (0.6429 * 0.75, 0.75 * 0.75))
    .lineTo(0.0, 0.75 * 0.75)
    .lineTo(0.0, 0.4286 * 0.75)
    .close()
    .extrude(-0.2246)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2246))
# --- Assembly ---
assembly = part_1
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1528.stl