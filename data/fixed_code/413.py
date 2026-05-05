import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0938 * 0.75  # Scaled width
part_1_height = 0.0141
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cutout ---
part_2_length = 0.0262 * 0.0262  # Scaled length
part_2_width = 0.0146 * 0.0262  # Scaled width
part_2_height = 0.016
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_413.stl