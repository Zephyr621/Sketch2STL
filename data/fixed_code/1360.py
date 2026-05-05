import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75   # Scaled width
height = 0.0225
hole_radius = 0.0112 * 0.75  # Scaled radius
hole_centers = [
    (0.125 * 0.75 - length/2, 0.125 * 0.75 - width/2),
    (0.125 * 0.75 - length/2, 0.625 * 0.75 - width/2),
    (0.625 * 0.75 - length/2, 0.125 * 0.75 - width/2),
    (0.625 * 0.75 - length/2, 0.625 * 0.75 - width/2)
]
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Cut the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1360.stl"output_1360.stl