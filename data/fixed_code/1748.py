import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0402)
    .threePointArc((0.6284, 0.0901), (0.375, 0.1095))
    .lineTo(0.2893, 0.1822)
    .lineTo(0.2893, 0.0872)
    .lineTo(0.3296, 0.0872)
    .lineTo(0.3296, 0.1436)
    .lineTo(0.4167, 0.1436)
    .threePointArc((0.2076, 0.0903), (0.2893, 0.1629))
    .lineTo(0.2893, 0.1779)
    .lineTo(0.0, 0.1779)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1436 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1748.stl