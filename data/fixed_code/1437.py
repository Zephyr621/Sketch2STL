import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0395 * 0.75  # Scaled width
part_1_length = 0.75 * 0.75  # Scaled length
part_1_height = 0.0248
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
assembly = assembly.translate((0, 0, 0.0148))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1437.stl