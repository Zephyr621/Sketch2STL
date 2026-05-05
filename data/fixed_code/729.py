import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.5455 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0205
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
cutout_length = 0.0125 * 0.75  # Scaled length
cutout_width = 0.75 * 0.75  # Scaled width
cutout_height = 0.0125
cutout = (
    cq.Workplane("XY")
    .rect(cutout_length, cutout_width)
    .extrude(-cutout_height)  # Extrude in the opposite direction for cutting
)
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_729.stl