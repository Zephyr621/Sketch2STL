import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.6774 * 0.75  # Scaled width
height = 0.0181
hole_radius = 0.0052 * 0.75  # Scaled radius
hole1_x = 0.1882 * 0.75  # Scaled x-coordinate
hole1_y = 0.0804 * 0.75  # Scaled y-coordinate
hole2_x = 0.5625 * 0.75  # Scaled x-coordinate
hole2_y = 0.1607 * 0.75  # Scaled y-coordinate
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_512.stl"output_512.stl