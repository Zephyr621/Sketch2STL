import cadquery as cq
# --- Part 1: U-shaped Bracket ---
part_1_width = 0.7482 * 0.75  # Scaled width
part_1_length = 0.75 * 0.75 # Scaled length
part_1_height = 0.4712
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_width, 0)
    .lineTo(part_1_width, part_1_length)
    .lineTo(0, part_1_length)
    .close()
    .extrude(-part_1_height)  # Extrude downwards for cutting
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4712, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2611.stl