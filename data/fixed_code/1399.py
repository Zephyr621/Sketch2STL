import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.75 * 0.75  # Scaled length
width = 0.2708 * 0.75  # Scaled width
height = 0.075 + 0.075  # Total height (extrusion in both directions)
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.3))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Final Result ---
result = assembly
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1399.stl