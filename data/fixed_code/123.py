import cadquery as cq
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75   # Scaled width
height = 0.0312
hole_radius = 0.0094 * 0.75  # Scaled radius
corner_offset = 0.0156 * 0.75  # Scaled offset for corner holes
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the corner holes ---
hole_locations = [
    (corner_offset - length/2, corner_offset - width/2),
    (corner_offset - length/2, width/2 - corner_offset),
    (length/2 - corner_offset, corner_offset - width/2),
]
for x, y in hole_locations:
    plate = plate.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_123.stl"output_123.stl