import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4375 * 0.75)
    .lineTo(0.6188 * 0.75, 0.4375 * 0.75)
    .threePointArc((0.3627 * 0.75, 0.2109 * 0.75), (0.3627 * 0.75, 0.4225 * 0.75))
    .lineTo(0.0, 0.4225 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0134 * 2 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0208))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_262.stl