import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.125 * 0.125  # Scaled length
part_1_width = 0.0417 * 0.125  # Scaled width
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Triangular Cutout ---
part_2_length = 0.125 * 0.125  # Scaled length
part_2_width = 0.0062 * 0.125  # Scaled width
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2517.stl