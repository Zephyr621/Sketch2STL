import cadquery as cq
# --- Part 1: L-shaped base ---
part_1_scale = 0.75
part_1_depth = 0.325
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.375 * part_1_scale, 0)
    .lineTo(0.375 * part_1_scale, 0.125 * part_1_scale)
    .lineTo(0.625 * part_1_scale, 0.125 * part_1_scale)
    .lineTo(0.625 * part_1_scale, 0.4 * part_1_scale)
    .lineTo(0.125 * part_1_scale, 0.4 * part_1_scale)
    .lineTo(0.125 * part_1_scale, 0.125 * part_1_scale)
    .close()
    .extrude(-part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.325))
# --- Part 2: Cube Cutout ---
part_2_scale = 0.32
part_2_depth =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1948.stl