import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.525 * 0.75  # Scaled width
height = 0.0188
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
# Find the vertical edges and apply fillets
edge_radius = min(length, width) / 10  # Adjust the divisor for desired fillet size
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
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_739.stl"output_739.stl