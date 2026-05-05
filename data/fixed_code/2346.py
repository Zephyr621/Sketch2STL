import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.4286 * 0.75  # Scaled width
height = 0.0214
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
edge_radius = min(length, width) / 10  # Adjust as needed; avoid large values
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2346.stl