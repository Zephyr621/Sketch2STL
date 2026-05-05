import cadquery as cq
# --- Part 1: Cube ---
cube_size = 0.75 * 0.75  # Sketch size scaled
cube_height = 0.75
part_1 = cq.Workplane("XY").box(cube_size, cube_size, cube_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
cutout_size = 0.75 * 0.75  # Sketch size scaled
cutout_depth = 0.375
part_2 = cq.Workplane("XY").box(cutout_size, cutout_size, cutout_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.75, 0))
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2)
cq.
# --- Export to STL ---
cq.cq.exporters.export(assembly,
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1674.stl