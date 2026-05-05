import cadquery as cq
from math import tan, radians
# --- Part 1: Cube with Hexagonal Hole ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.0937 * 0.75  # Scaled hole radius
extrude_depth = 0.2812
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_608.stl"output_608.stl