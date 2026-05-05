import cadquery as cq
# --- Part 1: Rectangular Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.6048 * 0.75  # Scaled width
plate_height = 0.0726
part_1 = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# --- Part 2: Holes ---
hole_radius = 0.0117 * 0.2667  # Scaled radius
hole_locations = [
    (0.0358 * 0.2667 - plate_length/2, 0.015 * 0.2667 - plate_width/2),  # Bottom Left
    (0.0358 * 0.2667 - plate_length/2, 0.3565 * 0.2667 - plate_width/2),  # Top Right
    (0.7395 * 0.2667 - plate_length/2, 0.015 * 0.2667 - plate_width/2),  # Bottom Right
]
for x, y in hole_locations:
    part_1 = part_1.faces(">Z").workplane().hole(2 * hole_radius)
# --- Assembly: Cut Holes from Plate ---
result = part_1
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_132.stl"output_132.stl