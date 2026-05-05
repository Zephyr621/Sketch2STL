import cadquery as cq
from math import radians
# --- Part 1: Torus Base ---
part_1_outer_radius = 0.375 * 0.75
part_1_inner_radius = 0.1988 * 0.75
part_1_height = 0.1193
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Central Hole ---
part_2_radius = 0.2545 * 0.545
part_2_depth = 0.1193
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.1193)
    .moveTo(0.1244, 0.1244)
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Assembly ---
assembly = part_1.translate((0, 0, 0.1193))
assembly = assembly.union(part_2.translate((0.2438, 0.2438, 0.1193)))
# --- Export to STL ---
cq.
cq.cq.exporters.export({result_var}, "output_152.stl"output_152.stl