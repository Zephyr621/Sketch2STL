import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.0352 * 0.0792  # Sketch radius scaled
inner_radius = 0.0288 * 0.0792  # Inner radius scaled
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
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_859.stl"output_859.stl