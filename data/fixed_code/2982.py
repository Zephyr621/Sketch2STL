import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.1312 * 0.2386  # Sketch radius scaled
inner_radius = 0.0599 * 0.2386  # Inner radius scaled
height = 0.1875 + 0.1875
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2982.stl"output_2982.stl