import cadquery as cq
# --- Part 1: Rectangular Beam ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0352 * 0.75  # Scaled width
part_1_height = 0.0352
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0352, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1011.stl