import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Square Plate with Holes ---
plate_size = 0.75 * 0.75  # Scaled plate size
hole_radius = 0.0356 * 0.75  # Scaled hole radius
corner_offset = 0.0565 * 0.75 # Scaled corner offset
plate_thickness = 0.0154
# Create the square plate
plate = cq.Workplane("XY").rect(plate_size, plate_size).extrude(plate_thickness)
# Add holes at the corners
hole_locations = [
    (corner_offset - plate_size/2, corner_offset - plate_size/2),
    (corner_offset - plate_size/2, plate_size/2 - corner_offset),
    (plate_size/2 - corner_offset, corner_offset - plate_size/2),
    (plate_size/2 - corner_offset, plate_size/2 - corner_offset)
]
for x, y in hole_locations:
    plate = plate.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# Export to STL
# Export to STL
cq.exporters.export({result_var}, "output_2077.stl"output_2077.stl