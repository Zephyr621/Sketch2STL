import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.25 * 0.25  # Scaled length
width = 0.05 * 0.25  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_590.stl"output_590.stl