import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.7031 * 0.75  # Scaled width
height = 0.0281
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Add holes
hole_radius = min(length, width) / 10  # Adjust as needed; avoid large values
part_1 = part_1.faces(">Z").workplane().hole(2 * hole_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to
# 导出为STL文件
cq.exporters.export(result, "output_2179.stl