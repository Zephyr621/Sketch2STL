import cadquery as cq
# --- Part 1: Base ---
part_1_width = 0.0375 * 0.0637  # Scaled width
part_1_length = 0.0637 * 0.0637 # Scaled length
part_1_height = 0.1875 + 0.1875  # Total height (both directions)
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_length).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Top Cube ---
part_2_size = 0.0938 * 0.0938  # Scaled size
part_2_height = 0.1875 + 0.1875  # Total height (both directions)
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3319.stl