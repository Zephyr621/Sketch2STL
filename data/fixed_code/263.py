import cadquery as cq
# --- Part 1: Base Square ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_height = 0.3699
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Part 2: Top Square (Join) ---
part_2_size = 0.75 * 0.75  # Scaled size
part_2_height = 0.2163
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)  # Extrude in the opposite direction for cutting
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0, part_1_height))
# --- Assembly: Join Part 2 onto Part 1 ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.exporters
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_263.stl