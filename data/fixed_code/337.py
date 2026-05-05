import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2938 * 0.6596)
    .lineTo(0.0743 * 0.6596, 0.0)
    .threePointArc((0.1071 * 0.6596, 0.0352 * 0.6596), (0.1824 * 0.6596, 0.0))
    .lineTo(0.1957 * 0.6596, 0.0)
    .lineTo(0.1844 * 0.6596, 0.2938 * 0.6596)
    .lineTo(0.1849 * 0.6596, 0.2938 * 0.6596)
    .lineTo(0.0179 * 0.6596, 0.2938 * 0.6596)
    .threePointArc((0.0076 * 0.6596, 0.6298 * 0.6596), (0.0, 0.2938 * 0.6596))
    .close()
    .extrude(0.75)
)
# --- Coordinate System
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_337.stl