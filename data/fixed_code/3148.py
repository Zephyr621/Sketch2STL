import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.6495 * 0.6495  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Fillet Edges ---
edge_radius = 0.05  # Adjust the fillet radius as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_3148.stl