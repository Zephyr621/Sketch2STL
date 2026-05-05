import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0352 * 0.75)
    .lineTo(0.6713 * 0.75, 0.0352 * 0.75)
    .lineTo(0.6713 * 0.75, 0.3348 * 0.75)
    .lineTo(0.1579 * 0.75, 0.3348 * 0.75)
    .lineTo(0.1579 * 0.75, 0.0352 * 0.75)
    .lineTo(0.0, 0.0352 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0962 + 0.0962)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_117.stl