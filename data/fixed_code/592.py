import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0179 * 0.3947)
    .lineTo(0.0286 * 0.3947, 0.0)
    .lineTo(0.3846 * 0.3947, 0.0)
    .lineTo(0.3846 * 0.3947, 0.0179 * 0.3947)
    .lineTo(0.3947 * 0.3947, 0.0179 * 0.3947)
    .lineTo(0.3947 * 0.3947, 0.0)
    .lineTo(0.3947 * 0.3947, 0.3947 * 0.3947)
    .lineTo(0.0, 0.3947 * 0.3947)
    .lineTo(0.0, 0.0179 * 0.3947)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_592.stl