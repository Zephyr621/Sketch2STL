import cadquery as cq
# --- Part 1: Cube with Holes ---
length = 0.75 * 0.75  # Scaled length
width = 0.2934 * 0.75  # Scaled width
height = 0.1786
hole_radius = 0.0704 * 0.75  # Scaled radius
hole1_x = 0.1364 * 0.75  # Scaled x-coordinate
hole1_y = 0.1442 * 0.75  # Scaled y-coordinate
hole2_x = 0.6226 * 0.75  # Scaled x-coordinate
hole2_y = 0.2885 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.cq.exporters.export({result_var}, "output_749.stl"output_749.stl