import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0631 * 0.75)
    .lineTo(0.6977 * 0.75, 0.0631 * 0.75)
    .lineTo(0.6977 * 0.75, 0.2432 * 0.75)
    .lineTo(0.7125 * 0.75, 0.2432 * 0.75)
    .lineTo(0.7125 * 0.75, 0.3189 * 0.75)
    .lineTo(0.75 * 0.75, 0.3189 * 0.75)
    .lineTo(0.75 * 0.75, 0.4286 * 0.75)
    .lineTo(0.0, 0.4286 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.25)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1184.stl