import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1691)
    .lineTo(0.5536, 0.1691)
    .lineTo(0.5536, 0.4586)
    .lineTo(0.2749, 0.4586)
    .lineTo(0.2749, 0.1691)
    .lineTo(0.0, 0.1691)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3333 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3333, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2447.stl