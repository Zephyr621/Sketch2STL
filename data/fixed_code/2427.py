import cadquery as cq
# --- Part 1: L-shaped Base ---
part_1_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.25 * part_1_scale, 0)
    .lineTo(0.25 * part_1_scale, 0.125 * part_1_scale)
    .lineTo(0.75 * part_1_scale, 0.125 * part_1_scale)
    .lineTo(0.75 * part_1_scale, 0.375 * part_1_scale)
    .lineTo(0, 0.375 * part_1_scale)
    .close()
    .extrude(0.25)
)
# --- Part 2: Cutout ---
part_2_scale = 0.5
cutout_size = 0.25 * part_2_scale
cutout_depth = 0.125 * part_2_scale
cutout = (
    cq.Workplane("XY")
    .rect(cutout_size, cutout_size)
    .extrude(-cutout_depth)
)
# --- Coordinate System Transformation for Part 1 ---
cutout = cutout.rotate((0, 0, 0), (0, 0, 1), -90)
cutout = cutout.translate((0, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2427.stl