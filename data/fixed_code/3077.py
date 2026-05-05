import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.15 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.225 * 0.75), (0.6 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.45 * 0.75)
    .lineTo(0.3 * 0.75, 0.45 * 0.75)
    .threePointArc((0.1924 * 0.75, 0.225 * 0.75), (0.0, 0.45 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.075)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.075, 0))
# --- Assembly ---
assembly = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3077.stl