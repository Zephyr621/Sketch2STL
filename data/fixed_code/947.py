import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1654 * 0.75)
    .lineTo(0.5833 * 0.75, 0.1654 * 0.75)
    .lineTo(0.5833 * 0.75, 0.2143 * 0.75)
    .lineTo(0.3857 * 0.75, 0.2143 * 0.75)
    .lineTo(0.3857 * 0.75, 0.2976 * 0.75)
    .lineTo(0.0, 0.2976 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0078)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0078, 0))
# --- Assembly ---
assembly = part_1
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_947.stl