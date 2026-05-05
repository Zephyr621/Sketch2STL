import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.6625 * 0.6625  # Sketch length scaled
part_1_width = 0.6625 * 0.6625  # Sketch width scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cutout ---
part_2_length = 0.4125 * 0.4125  # Sketch length scaled
part_2_width = 0.2 * 0.4125  # Sketch width scaled
part_2_height = 0.5
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0844, 0, 0.0844))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
cq
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_244.stl