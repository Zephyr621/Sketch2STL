import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.5529 * 0.75  # Scaled width
height = 0.0021
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0.0542 * 0.75, width)
    .lineTo(0.0542 * 0.75, 0.6643 * 0.75)
    .lineTo(0, 0.6643 * 0.75)
    .close()
    .extrude(height)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_708.stl"output_708.stl