import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.025 * 0.05  # Sketch radius scaled
inner_radius = 0.0225 * 0.05  # Inner radius scaled
height = 0.1875 + 0.1875
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1576.stl"output_1576.stl