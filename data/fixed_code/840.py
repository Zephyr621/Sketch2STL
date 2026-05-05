import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.4687 * 0.75  # Scaled width
height = 0.4687
part_1 = cq.Workplane("XY").box(length, width, height)
# --- Create Rounded Edges ---
edge_radius = min(length, width, height) / 10  # Example radius, adjust as needed
part_1 = part_1.edges(">Z or <Z").fillet(edge_radius)
part_1 = part_1.edges("<Z or >Z").fillet(edge_radius)
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
cq.
cq.cq.exporters.export({result_var}, "output_840.stl"output_840.stl