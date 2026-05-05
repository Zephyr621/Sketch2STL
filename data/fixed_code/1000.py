import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.7152 * 0.75  # Sketch width scaled
part_1_height = 0.1875
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cutout ---
part_2_length = 0.0725 * 0.1784  # Sketch length scaled
part_2_width = 0.1784 * 0.1784  # Sketch width scaled
part_2_height = 0.0962
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0263, 0.0263, 0.1875))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.exporters
# 导出为STL文件
cq.exporters.export(result, "output_1000.stl