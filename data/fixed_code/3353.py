import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.6875 * 0.75  # Scaled width
height = 0.125 + 0.125
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.125, 0))
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust radius as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3353.stl"output_3353.stl