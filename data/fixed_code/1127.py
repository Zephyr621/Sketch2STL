import cadquery as cq
# --- Parameters from JSON ---
length = 0.3014 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0119
hole_radius = 0.0058 * 0.75  # Scaled radius
hole_centers = [
    (0.1541 * 0.75 - length/2, 0.1677 * 0.75 - width/2),
    (0.1541 * 0.75 - length/2, 0.6328 * 0.75 - width/2),
    (0.1721 * 0.75 - length/2, 0.1677 * 0.75 - width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Cut the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1127.stl"output_1127.stl