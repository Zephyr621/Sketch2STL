import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0411 * 0.0411  # Sketch width scaled
part_1_height = 0.0154
part_1_length = 0.75
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_length).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cube ---
part_2_size = 0.0527 * 0.0527  # Sketch size scaled
part_2_height = 0.0208
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2903.stl