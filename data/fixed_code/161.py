import cadquery as cq
# --- Part 1: Base with Cutout ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3571 * 0.75  # Scaled width
part_1_height = 0.1429
cutout_x_start = 0.1582 * 0.75
cutout_y_start = 0.1758 * 0.75
cutout_width = (0.5159 - 0.1758) * 0.75
cutout_height = (0.3393 - 0.1758) * 0.75
base = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).translate((cutout_x_start - part_1_length/2 + cutout_width/2, cutout_y_start - part_1_width/2 + cutout_height/2, 0)).extrude(part_1_height + 0.1)
base = base.cut(cutout)
# --- Part 2: Rectangular Block with Cutout ---
part_2_length = 0.3214 * 0
# Export
# 定义结果变量
result = cutout
# 导出为STL文件
cq.exporters.export(result, "output_161.stl