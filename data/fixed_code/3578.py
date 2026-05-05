import cadquery as cq
# --- Part 1: Rectangular Plate with Hole ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.3 * 0.75  # Scaled width
plate_height = 0.075
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.15 * 0.75  # Scaled center y
hole_radius = 0.0375 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - plate_length/2, hole_center_y - plate_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3578.stl"output_3578.stl