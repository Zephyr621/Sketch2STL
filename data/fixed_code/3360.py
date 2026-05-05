import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.5769 * 0.75  # Scaled width
height = 0.0156
hole_radius = 0.0078 * 0.75  # Scaled hole radius
hole_centers = [
    (0.1083 * 0.75 - length/2, 0.2067 * 0.75 - width/2),
    (0.1083 * 0.75 - length/2, 0.5114 * 0.75 - width/2),
    (0.6442 * 0.75 - length/2, 0.2067 * 0.75 - width/2),
    (0.6442 * 0.75 - length/2, 0.5114 * 0.75 - width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_3360.stl"output_3360.stl