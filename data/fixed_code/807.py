import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Box ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2769 * 0.75)
    .threePointArc((0.7415 * 0.75, 0.5354 * 0.75), (0.5739 * 0.75, 0.5353 * 0.75))
    .lineTo(0.5184 * 0.75, 0.2769 * 0.75)
    .lineTo(0.5184 * 0.75, 0.5403 * 0.75)
    .lineTo(0.0, 0.5403 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2323)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2323, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_807.stl