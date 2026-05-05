import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0427 * 0.75  # Scaled width
part_1_height = 0.007 * 0.75  # Scaled height
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.007, 0))
# --- Part 2: Cutout Cube ---
part_2_size = 0.7456 * 0.7456  # Scaled size
part_2_depth = 0.0015 * 0.7456  # Scaled depth
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0,
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_212.stl