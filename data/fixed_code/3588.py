import cadquery as cq
# --- Part 1: Cube with Diagonal Cut ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1429 * 0.75)
    .lineTo(0.6429 * 0.75, 0.1429 * 0.75)
    .lineTo(0.6429 * 0.75, 0.3214 * 0.75)
    .lineTo(0.2586 * 0.75, 0.3214 * 0.75)
    .lineTo(0.2586 * 0.75, 0.1071 * 0.75)
    .lineTo(0.0536 * 0.75, 0.1071 * 0.75)
    .lineTo(0.0536 * 0.75, 0.0493 * 0.75)
    .lineTo(0.0, 0.0493 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.2143)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3588.stl