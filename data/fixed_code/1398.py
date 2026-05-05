import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Sketch length scaled
width = 0.375 * 0.75  # Sketch width scaled
height = 0.0536
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Apply fillets to top edges ---
# Find edges to fillet (all edges along the top face)
edge_selector = "|Z"  # Select edges parallel to the Z-axis
fillet_radius = min(length, width) / 10  # Adjust fillet radius as needed
part_1 = part_1.edges(edge_selector).fillet(fillet_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0268))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1398.stl"output_1398.stl