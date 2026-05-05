import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0469 * 0.75)
    .lineTo(0.6814 * 0.75, 0.0469 * 0.75)
    .lineTo(0.6814 * 0.75, 0.3542 * 0.75)
    .lineTo(0.4286 * 0.75, 0.3542 * 0.75)
    .lineTo(0.4286 * 0.75, 0.0893 * 0.75)
    .lineTo(0.2511 * 0.75, 0.0893 * 0.75)
    .lineTo(0.2511 * 0.75, 0.1713 * 0.75)
    .lineTo(0.0, 0.1713 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0916 + 0.0916)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2129.stl