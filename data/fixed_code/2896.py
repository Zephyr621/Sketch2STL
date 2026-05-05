import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2748 * 0.621)
    .lineTo(0.2619 * 0.621, 0.2748 * 0.621)
    .lineTo(0.2619 * 0.621, 0.2308 * 0.621)
    .lineTo(0.4341 * 0.621, 0.2308 * 0.621)
    .lineTo(0.4341 * 0.621, 0.0)
    .lineTo(0.3102 * 0.621, 0.0)
    .lineTo(0.3102 * 0.621, 0.2748 * 0.621)
    .lineTo(0.0, 0.2748 * 0.621)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2896.stl