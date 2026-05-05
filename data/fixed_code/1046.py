import cadquery as cq
# --- Part 1: Rectangular Bar ---
part_1_length = 0.0311 * 0.0311  # Scaled length
part_1_width = 0.0208 * 0.0311   # Scaled width
part_1_height = 0.1875 + 0.1875  # Total height from extrusion
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
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
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1046.stl