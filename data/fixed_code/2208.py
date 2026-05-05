import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.649 * 0.75  # Scaled width
part_1_height = 0.0029
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Part 2: Cutout ---
part_2_length = 0.6136 * 0.6136  # Scaled length
part_2_width = 0.0469 * 0.6136  # Scaled width
part_2_height = 0.0167
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0386, 0.0811, part_1_height))
# --- Part 3: Join Feature ---
part_3_length = 0.6136 * 0.6136  # Scaled length
part_3_width = 0.0469 * 0.6136  # Scaled width
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2208.stl