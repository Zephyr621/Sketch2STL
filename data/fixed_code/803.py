import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.3409 * 0.75  # Scaled width
height = 0.0165
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Fillet Edges ---
# Select all vertical edges and apply fillets
fillet_radius = min(length, width) / 10  # Adjust fillet radius as needed
part_1 = part_1.edges("|Z").fillet(fillet_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_803.stl