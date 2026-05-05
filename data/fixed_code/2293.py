import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.2792 * 0.5294  # Sketch radius scaled
inner_radius = 0.1339 * 0.5294  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
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
# Export to STL
cq.cq.exporters.export({result_var}, "output_2293.stl"output_2293.stl