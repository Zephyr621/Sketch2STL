import cadquery as cq
from cadquery import exporters
# --- Part 1: Curved Base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1875 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.1875 * 0.75), (0.5625 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.5625 * 0.75, 0.375 * 0.75)
    .lineTo(0.5625 * 0.75, 0.1875 * 0.75)
    .lineTo(0.1875 * 0.75, 0.1875 * 0.75)
    .lineTo(0.1875 * 0.75, 0.375 * 0.75)
    .lineTo(0.0, 0.375 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0647)
)
# Add holes to Part 1
hole_radius = 0.0562 * 0.75
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1678.stl