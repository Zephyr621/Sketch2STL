import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.3359 * 0.75  # Scaled width
height = 0.0161  # Height
part_1 = cq.Workplane("XY").box(length, width, height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0161, 0))
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
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_3550.stl"output_3550.stl