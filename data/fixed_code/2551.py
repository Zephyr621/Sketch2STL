import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.3459 * 0.75  # Scaled width
height = 0.0417
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0417))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2551.stl"output_2551.stl