import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0469
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Ring ---
outer_radius = 0.2893 * 0.5786
inner_radius = 0.2143 * 0.5786
ring_height = 0.0536
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(-ring_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0188, 0, 0.0188))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2834.stl"output_2834.stl