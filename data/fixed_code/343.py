import cadquery as cq
# --- Part 1: Square Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.021
hole_radius = 0.0058 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
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
# Export to STL
# 导出为STL文件
cq.exporters.export(result, "output_343.stl