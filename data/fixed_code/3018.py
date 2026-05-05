import cadquery as cq
# --- Part 1: Ring ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3281 * 0.75
height = 0.1562
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1562, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3018.stl"output_3018.stl