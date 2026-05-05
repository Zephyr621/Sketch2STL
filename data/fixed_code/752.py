import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.407 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0271
hole_radius = 0.0136 * 0.75  # Scaled radius
hole_centers = [
    (0.0727 * 0.75 - length / 2 + length/2, 0.0332 * 0.75 - width / 2 + width/2),
    (0.0727 * 0.75 - length / 2 + length/2, 0.7395 * 0.75 - width / 2 + width/2),
    (0.375 * 0.75 - length / 2 + length/2, 0.7395 * 0.75 - width / 2 + width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_752.stl"output_752.stl