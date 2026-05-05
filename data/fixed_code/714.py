import cadquery as cq
# --- Part 1: L-shaped base ---
part_1_scale = 0.75
part_1_depth = 0.6667
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.05 * part_1_scale, 0)
    .lineTo(0.05 * part_1_scale, 0.0083 * part_1_scale)
    .lineTo(0.7 * part_1_scale, 0.0083 * part_1_scale)
    .lineTo(0.7 * part_1_scale, 0.0194 * part_1_scale)
    .lineTo(0.05 * part_1_scale, 0.0194 * part_1_scale)
    .lineTo(0, 0.0194 * part_1_scale)
    .close()
    .extrude(-part_1_depth)
)
# --- Part 2: Rectangular protrusion ---
part_2_scale = 0.6167
part_2_depth = 0.0194
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.05
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_714.stl