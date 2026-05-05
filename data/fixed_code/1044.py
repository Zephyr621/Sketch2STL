import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.4845 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.25))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
assembly = assembly.rotate((0, 0, 0), (0, 0, 1), -90)
assembly = assembly.translate((0, 0, 0))
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1044.stl