import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Sketch length scaled
width = 0.2679 * 0.75  # Sketch width scaled
height = 0.1875 + 0.1875
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
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
cq.cq.exporters.export({result_var}, "output_1259.stl"output_1259.stl