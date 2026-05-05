import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.375 * 0.75 # Sketch height scaled
part_1_depth = 0.375
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_height).extrude(part_1_depth)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cube (Cutout) ---
part_2_width = 0.5 * 0.5  # Sketch width scaled
part_2_height = 0.5 * 0.5  # Sketch height scaled
part_2_depth = 0.25
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_height).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.125, 0.375, 0.125))
# --- Assembly: Cut Part 2
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2053.stl