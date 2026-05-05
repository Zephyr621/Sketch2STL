import cadquery as cq
# --- Part 1: Square Plate with Hole ---
plate_size = 0.75 * 0.75  # Scaled size
hole_radius = 0.0312 * 0.75  # Scaled radius
plate_thickness = 0.0625
part_1 = (
    cq.Workplane("XY")
    .rect(plate_size, plate_size)
    .extrude(plate_thickness)
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
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2030.stl"output_2030.stl