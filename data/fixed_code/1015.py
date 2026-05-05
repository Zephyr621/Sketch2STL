import cadquery as cq
from math import radians
# --- Part 1: Square Base ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_height = 0.1
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Part 2: Holes ---
hole_radius = 0.0065 * 0.7159
hole_depth = 0.02
hole_centers = [
    (0.0155, 0.0155),
    (0.0155, 0.5279),
    (0.5467, 0.0155),
    (0.5467, 0.5279)
]
for center_x, center_y in hole_centers:
    part_2 = part_1.faces(">Z").workplane().moveTo(center_x - part_1_size/2, center_y - part_1_size/2).circle(hole_radius).cutThruAll()
# --- Assembly ---
assembly = part_1.translate((0, 0, 0.0471))
# --- Export to STL ---
cq.
cq.cq.exporters.export({result_var}, "output_1015.stl"output_1015.stl