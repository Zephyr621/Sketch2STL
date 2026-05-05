import cadquery as cq
# --- Part 1: Rectangular Beam ---
part_1_length = 0.0461 * 0.0911  # Scaled length
part_1_width = 0.0911 * 0.0911   # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cutout ---
part_2_length = 0.0833 * 0.0833  # Scaled length
part_2_width = 0.0341 * 0.0833   # Scaled width
part_2_height = 0.0266
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(part_2_length
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_30.stl