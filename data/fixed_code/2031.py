import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.0945 * 0.75  # Scaled width
height = 0.0178
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
# Find the vertical edges and apply fillets
edge_selector = "|Z"  # Select edges parallel to the Z-axis (vertical edges)
fillet_radius = min(length, width) / 10  # Adjust fillet radius as needed
part_1 = part_1.edges(edge_selector).fillet(fillet_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2031.stl"output_2031.stl