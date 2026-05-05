import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.1875 * 0.75  # Scaled width
height = 0.0094
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
edge_radius = min(length, width) / 10  # Example fillet radius (adjust as needed)
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3220.stl"output_3220.stl