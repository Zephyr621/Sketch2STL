import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0937 * 0.75, 0.0)
    .lineTo(0.0937 * 0.75, 0.0469 * 0.75)
    .lineTo(0.6563 * 0.75, 0.0469 * 0.75)
    .lineTo(0.6563 * 0.75, 0.0938 * 0.75)
    .lineTo(0.75 * 0.75, 0.0938 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.375 * 0.75, 0.375 * 0.75)
    .lineTo(0.375 * 0.75, 0.5625 * 0.75)
    .lineTo(0.0, 0.5625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1875)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1247.stl