import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(-part_1_height)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Block ---
part_2_size = 0.25 * 0.5  # Sketch size scaled
part_2_height = 0.375
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0, 0.125))
# --- Part 3: Cutout ---
part_3_width = 0.25 * 0.5  # Sketch width scaled
part_3_height = 0.125
part
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2729.stl