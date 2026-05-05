import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25, 0.0)
    .threePointArc((0.5675 * 0.75, 0.0837 * 0.75), (0.75 * 0.75, 0.15 * 0.75))
    .lineTo(0.75 * 0.75, 0.3214 * 0.75)
    .threePointArc((0.5675 * 0.75, 0.1687 * 0.75), (0.25 * 0.75, 0.3214 * 0.75))
    .lineTo(0.25 * 0.75, 0.3 * 0.75)
    .threePointArc((0.2665 * 0.75, 0.1974 * 0.75), (0.0, 0.3 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0429)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_4.stl