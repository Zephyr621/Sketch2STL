import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5172 * 0.75  # Scaled width
part_1_height = 0.0098
cutout_x_start = 0.0911 * 0.75
cutout_y_start = 0.2574 * 0.75
cutout_width = (0.5455 - 0.0911) * 0.75
cutout_height = (0.2769 - 0.2574) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
cutout = (
    cq.Workplane("XY")
    .moveTo(cutout_x_start + cutout_width/2, cutout_y_start + cutout_height/2)
    .rect(cutout_width, cutout_height)
    .extrude(part_1_height)
)
part_1 = part_1.cut(cutout)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0098,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1476.stl