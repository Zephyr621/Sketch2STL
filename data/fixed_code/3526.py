import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Handle ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3254 * 0.75
height = 0.0268
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3526.stl"output_3526.stl