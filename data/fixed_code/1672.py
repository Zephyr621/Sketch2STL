import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0562 * 0.75)
    .lineTo(0.1969 * 0.75, 0.0562 * 0.75)
    .threePointArc((0.3947 * 0.75, 0.0188 * 0.75), (0.5357 * 0.75, 0.0))
    .lineTo(0.6179 * 0.75, 0.0)
    .threePointArc((0.6848 * 0.75, 0.0188 * 0.75), (0.75 * 0.75, 0.0562 * 0.75))
    .lineTo(0.75 * 0.75, 0.4286 * 0.75)
    .lineTo(0.0, 0.4286 * 0.75)
    .lineTo(0.0, 0.0562 * 0.75)
    .close()
    .extrude(0.0875)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1672.stl