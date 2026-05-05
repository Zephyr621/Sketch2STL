import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Part 2: Cutout ---
part_2_width = 0.6 * 0.6  # Sketch width scaled
part_2_depth = 0.6 * 0.6  # Sketch depth scaled
part_2_height = 0.675
part_2 = cq.Workplane("XY").box(part_2_width, part_2_depth, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.075, 0.75, 0))
# --- Part 3: Cutout 2 ---
part_3_width = 0.6 * 0.6  # Sketch width scaled
part_3_depth = 0.6 * 0.6  # Sketch depth scaled
part_3_height = 0.675
part_3 = cq.Workplane("XY").box(part_3_width, part_3_depth, part_3_height)
# --- Coordinate System Transformation for Part 3 ---
part
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_2415.stl