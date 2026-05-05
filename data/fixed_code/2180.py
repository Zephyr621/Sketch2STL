import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.5192 * 0.75, 0.4687 * 0.75)
    .lineTo(0.5192 * 0.75, 0.3409 * 0.75)
    .lineTo(0.2589 * 0.75, 0.3409 * 0.75)
    .lineTo(0.2589 * 0.75, 0.5407 * 0.75)
    .lineTo(0.0, 0.5407 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0536)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2180.stl