import cadquery as cq
# --- Parameters from JSON ---
length = 0.5625 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0197
hole_radius = 0.0208 * 0.75  # Scaled radius
hole1_x = 0.2125 * 0.75  # Scaled x position
hole1_y = 0.5 * 0.75  # Scaled y position
hole2_x = 0.2125 * 0.75  # Scaled x position
hole2_y = 0.625 * 0.75  # Scaled y position
# --- Create the rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(hole_radius * 2)
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2234.stl"output_2234.stl