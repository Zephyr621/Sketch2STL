import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.5294 * 0.75  # Scaled width
height = 0.7031
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Apply rotation and translation ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.7031, 0))
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
part_1 = part_1.edges(">Z or <Z").fillet(edge_radius)
# --- Export to STL ---
cq.
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
# 导出为STL文件
cq.exporters.export(result, "output_2796.stl