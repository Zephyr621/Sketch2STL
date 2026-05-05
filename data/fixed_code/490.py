import cadquery as cq
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.225
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cube ---
part_2_length = 0.225 * 0.225  # Scaled length
part_2_width = 0.225 * 0.225  # Scaled width
part_2_height = 0.225
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(part_2_height)
part_2 = part_2.translate((0, 0, 0.225))
# --- Part 3: Cutout ---
part_3_size = 0.075 * 0.675  # Scaled size
part_3_depth = 0.4687
part_3 = cq.Workplane("XY").
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_490.stl