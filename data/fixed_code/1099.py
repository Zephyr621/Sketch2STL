import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.75 * 0.75  # Scaled length
width = 0.4167 * 0.75  # Scaled width
height = 0.1816
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.75))
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
cq.
cq.cq.exporters.export({result_var}, "output_1099.stl"output_1099.stl