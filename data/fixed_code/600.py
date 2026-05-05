import cadquery as cq
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.225 * 0.75   # Scaled width
part_1_height = 0.1031
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cutout ---
part_2_length = 0.375 * 0.375  # Scaled length
part_2_width = 0.1462 * 0.375   # Scaled width
part_2_height = 0.0235
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)  # Extrude in the opposite direction for cutting
# --- Part 3: Small Cylinder ---
part_3_radius = 0.0236 * 0.0586  # Scaled radius
part_3_height = 0.0359
part_3 = cq.Workplane
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_600.stl