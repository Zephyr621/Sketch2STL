import cadquery as cq
# --- Part 1: Base Cube ---
part_1_size = 0.75 * 0.75  # Scale the size
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_size)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout 1 ---
part_2_size = 0.375 * 0.375  # Scale the size
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_size)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_62.stl