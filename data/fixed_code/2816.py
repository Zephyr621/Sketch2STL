import cadquery as cq
from math import radians
# --- Part 1: Rectangular Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.3125 * 0.75  # Scaled width
plate_height = 0.0156
part_1 = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# --- Part 2: Holes ---
hole_radius = 0.0094 * 0.7188  # Scaled radius
hole_depth = 0.0156
# Hole positions (scaled and translated)
hole_positions = [
    (-plate_length / 2 + hole_radius, -plate_width / 2 + hole_radius),
    (-plate_length / 2 + hole_radius, plate_width / 2 - hole_radius),
    (plate_length / 2 - hole_radius, plate_width / 2 - hole_radius),
]
# Create holes by cutting cylinders
for x, y in hole_positions:
    part_1 = part_1.faces(">Z").workplane().hole(2 * hole_depth)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2816.stl"output_2816.stl