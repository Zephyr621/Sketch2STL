import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1235 * 0.2579, 0.0)
    .lineTo(0.1235 * 0.2579, 0.0261 * 0.2579)
    .lineTo(0.0622 * 0.2579, 0.0261 * 0.2579)
    .lineTo(0.0622 * 0.2579, 0.1071 * 0.2579)
    .lineTo(0.0622 * 0.2579, 0.2579 * 0.2579)
    .lineTo(0.0, 0.2579 * 0.2579)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0011)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0011))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.1235 * 0.2579, 0.2579 * 0.2579)
    .extrude(-0.0156)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_971.stl