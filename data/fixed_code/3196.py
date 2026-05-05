import cadquery as cq
# --- Part 1: Square Plate ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.7223 * 0.75  # Sketch width scaled
part_1_height = 0.0092
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Fillet Edges ---
edge_radius = min(part_1_length, part_1_width) / 10  # Adjust as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3196.stl"output_3196.stl