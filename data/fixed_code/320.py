import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.3596 * 0.75  # Scaled width
height = 0.0089
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0089, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
try:
    assembly = assembly.edges("|Z").fillet(edge_radius)
except:
    print("Fillet operation failed. Continuing without fillets.")
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_320.stl"output_320.stl