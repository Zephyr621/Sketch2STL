import cadquery as cq
# --- Part 1: Square Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.75 * 0.75   # Scaled width
plate_height = 0.0121
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
)
# Add rounded corners
corner_radius = min(plate_length, plate_width) / 10  # Adjust as needed; avoid large values
part_1 = part_1.edges("|Z").fillet(corner_radius)
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
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2106.stl