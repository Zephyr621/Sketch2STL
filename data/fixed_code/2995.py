import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3333 * 0.75  # Scaled width
part_1_height = 0.0014
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0014, 0))
# --- Part 2: Cut Feature ---
part_2_length = 0.3886 * 0.3886  # Scaled length
part_2_width = 0.0417 * 0.3886  # Scaled width
part_2_height = 0.0014
cut_feature = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
# Export
# 定义结果变量
result = cut_feature
# 导出为STL文件
cq.exporters.export(result, "output_2995.stl