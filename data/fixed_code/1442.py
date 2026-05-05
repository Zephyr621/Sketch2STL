import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.225 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.1875
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1875))
# --- Part 2: Square Top ---
part_2_size = 0.1125 * 0.1125  # Scaled size
part_2_height = 0.1875
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.
cq.
cq.cq.exporters.export(assembly,
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1442.stl