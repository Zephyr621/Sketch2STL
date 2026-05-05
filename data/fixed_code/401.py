import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.5 * 0.75  # Scaled width
height = 0.025
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Fillet Edges ---
# Select edges for filleting (adjust selector if needed)
edge_selector = "|Z"  # Select all vertical edges
fillet_radius = min(length, width) / 10  # Example fillet radius, adjust as needed
part_1 = part_1.edges(edge_selector).fillet(fillet_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_401.stl"output_401.stl