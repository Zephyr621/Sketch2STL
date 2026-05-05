import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.0117 * 0.0469  # Scaled length
part_1_width = 0.0469 * 0.0469  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_344.stl