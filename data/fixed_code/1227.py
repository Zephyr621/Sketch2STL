import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.1797 * 0.2311  # Scaled length
part_1_width = 0.2323 * 0.2311  # Scaled width
part_1_height = 0.1838
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0014, 0.0014, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1227.stl