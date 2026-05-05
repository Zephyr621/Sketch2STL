import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.3614 * 0.75  # Scaled width
height = 0.0476
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Fillet Edges ---
# Select all edges along the top face (">Z")
edge_selector = "|Z"  # Select edges parallel to the Z-axis (vertical edges)
fillet_radius = min(length, width) / 10  # Adjust fillet radius as needed
part_1 = part_1.edges(edge_selector).fillet(fillet_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to
# 导出为STL文件
cq.exporters.export(result, "output_1191.stl