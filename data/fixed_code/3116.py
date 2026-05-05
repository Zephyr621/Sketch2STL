import cadquery as cq
# --- Part 1: Base Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.5156
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Part 2: Top Cube ---
part_2_size = 0.75 * 0.75  # Sketch size scaled
part_2_height = 0.15
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0, part_1_height))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3116.stl