import cadquery as cq
from cadquery.vis import show
# --- Part 1: Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.0714 * 0.75
height = 0.0368
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Part 2: Cylinder ---
outer_radius_2 = 0.1071 * 0.2072
inner_radius_2 = 0.0714 * 0.2072
height_2 = 0.0268
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius_2)
    .extrude(height_2)
    .cut(cq.Workplane("XY").circle(inner_radius_2).extrude(height_2))
)
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1459.stl"output_1459.stl