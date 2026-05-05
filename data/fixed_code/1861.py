import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.5306
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Fillet Edges ---
edge_radius = min(part_1_size/2, part_1_height/2)  # Adjust as needed for desired roundness
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1861.stl"output_1861.stl