import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3439 * 0.75, 0.0)
    .threePointArc((0.3735 * 0.75, 0.1295 * 0.75), (0.7246 * 0.75, 0.1299 * 0.75))
    .lineTo(0.4653 * 0.75, 0.2452 * 0.75)
    .threePointArc((0.3736 * 0.75, 0.375 * 0.75), (0.3665 * 0.75, 0.2452 * 0.75))
    .lineTo(0.2348 * 0.75, 0.2452 * 0.75)
    .threePointArc((0.1516 * 0.75, 0.375 * 0.75), (0.1868 * 0.75, 0.1299 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1419.stl