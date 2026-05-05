import cadquery as cq
# --- Part 1: Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.4482 * 0.75  # Scaled width
height = 0.0094
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_978.stl"output_978.stl