import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.7344
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Apply fillets to all edges
edge_radius = min(length, width, height) / 10  # Adjust radius as needed
part_1 = part_1.edges().fillet(edge_radius)
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
cq.cq.exporters.export({result_var}, "output_1592.stl"output_1592.stl