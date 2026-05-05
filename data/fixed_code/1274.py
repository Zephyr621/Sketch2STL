import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0794 * 0.0872, 0.0)
    .lineTo(0.0794 * 0.0872, 0.0269 * 0.0872)
    .threePointArc((0.0352 * 0.0872, 0.0424 * 0.0872), (0.0112 * 0.0872, 0.0269 * 0.0872))
    .lineTo(0.0112 * 0.0872, 0.0017 * 0.0872)
    .lineTo(0.0017 * 0.0872, 0.0017 * 0.0872)
    .threePointArc((0.0438 * 0.0872, 0.0448 * 0.0872), (0.0112 * 0.0872, 0.0))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1274.stl