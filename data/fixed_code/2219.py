import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_radius = 0.0458 * 0.0816  # Sketch radius scaled
inner_radius = 0.0272 * 0.0816  # Inner hole radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_2219.stl"output_2219.stl