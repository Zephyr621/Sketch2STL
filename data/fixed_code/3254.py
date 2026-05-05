import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0313 * 0.75, 0.0)
    .lineTo(0.7135 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1858 * 0.75)
    .lineTo(0.75 * 0.75, 0.2679 * 0.75)
    .lineTo(0.7135 * 0.75, 0.2679 * 0.75)
    .lineTo(0.7135 * 0.75, 0.1043 * 0.75)
    .lineTo(0.0313 * 0.75, 0.1043 * 0.75)
    .lineTo(0.0313 * 0.75, 0.2679 * 0.75)
    .lineTo(0.0, 0.2679 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0125)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3254.stl