import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.1607 * 0.75  # Scaled width
height = 0.25
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Fillet Edges ---
# Select edges to fillet (all edges along Z-axis)
edge_selector = "|Z"  # Select edges parallel to the Z-axis
fillet_radius = min(length, width, height) / 10  # Adjust fillet radius as needed
assembly = assembly.edges(edge_selector).fillet(fillet_radius)
# --- Apply Translation ---
assembly = assembly.translate((0, 0, 0.25))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_3361.stl"output_3361.stl