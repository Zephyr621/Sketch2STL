import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.4687 * 0.75  # Scaled width
height = 0.0155
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed; avoid large values
part_1 = part_1.edges("|Z").fillet(edge_radius)
part_1 = part_1.edges(">Z or <Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2653.stl"output_2653.stl