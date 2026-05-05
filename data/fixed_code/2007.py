import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.5
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.5))
# --- Part 2: Cutout ---
part_2_length = 0.25 * 0.25  # Scaled length
part_2_width = 0.125 * 0.25  # Scaled width
part_2_height = 0.25
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.25, 0.125, 0.5))
# --- Assembly: Cut Part 2 from Part 1 ---
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2007.stl