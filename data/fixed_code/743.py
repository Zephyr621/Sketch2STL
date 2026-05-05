import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.3125)
    .lineTo(0.5, 0.3125)
    .lineTo(0.5, 0.4375)
    .lineTo(0.25, 0.4375)
    .lineTo(0.25, 0.6188)
    .lineTo(0.0, 0.6188)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3409 * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1781))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_743.stl