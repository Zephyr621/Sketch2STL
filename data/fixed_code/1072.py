import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3125 * 0.75  # Inner radius scaled
height = 0.2362
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2362, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.cq.exporters.export({result_var}, "output_1072.stl"output_1072.stl