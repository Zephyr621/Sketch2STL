import cadquery as cq
# --- Part 1: Base Cube ---
part_1_length = 0.75 * 0.75
part_1_width = 0.5 * 0.75
part_1_height = 0.4167
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Top Square ---
part_2_length = 0.25 * 0.25
part_2_width = 0.25 * 0.25
part_2_height = 0.3333
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1667, 0, 0.1667))
# --- Part 3: Bottom Square ---
part_3_length = 0.25 * 0.25
part_3_width = 0.25 * 0.25
part_
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1818.stl