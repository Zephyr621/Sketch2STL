import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.15 * 0.75)
    .lineTo(0.525 * 0.75, 0.15 * 0.75)
    .lineTo(0.525 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.15 * 0.75)
    .lineTo(0.6 * 0.75, 0.15 * 0.75)
    .lineTo(0.6 * 0.75, 0.0)
    .lineTo(0.525 * 0.75, 0.0)
    .lineTo(0.225 * 0.75, 0.15 * 0.75)
    .lineTo(0.225 * 0.75, 0.0)
    .close()
    .extrude(-0.75 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_36.stl