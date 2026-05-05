import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.6207)
    .lineTo(0.5717, 0.6207)
    .lineTo(0.5717, 0.5472)
    .lineTo(0.1879, 0.5472)
    .lineTo(0.1879, 0.6548)
    .lineTo(0.1879, 0.6071)
    .lineTo(0.0, 0.6071)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0008 * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0872, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3505.stl