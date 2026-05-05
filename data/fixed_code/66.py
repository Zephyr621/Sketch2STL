import cadquery as cq
# --- Part 1: Rectangular Plate with Holes ---
length = 0.75 * 0.75  # Scaled length
width = 0.5351 * 0.75  # Scaled width
height = 0.0361  # Height
hole_radius = 0.0166 * 0.75  # Scaled hole radius
hole1_x = 0.1071 * 0.75  # Scaled hole x position
hole2_y = 0.2529 * 0.75  # Scaled hole y position
hole_radius = 0.0563 * 0.75  # Scaled hole radius
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(hole_radius * 2)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.cq.exporters.export({result_var}, "output_66.stl"output_66.stl