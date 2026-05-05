import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.525
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.525, 0))
# --- Part 2: Ring ---
outer_radius = 0.375 * 0.75  # Outer radius scaled
inner_radius = 0.3125 * 0.75  # Inner radius scaled
part_2_height = 0.15
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.525, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_666.stl"output_666.stl