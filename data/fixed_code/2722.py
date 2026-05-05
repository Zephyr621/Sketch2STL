import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.7499 * 0.7499  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
part_2_size = 0.75 * 0.75  # Sketch size scaled
part_2_height = 0.5207
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0, 0.1071))
# --- Part 3: Circular Hole ---
part_3_radius = 0.0244 * 0.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2722.stl