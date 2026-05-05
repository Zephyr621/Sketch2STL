import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.75 * 0.75  # Scaled length
width = 0.6525 * 0.75  # Scaled width
height = 0.4125
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4125, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_357.stl"output_357.stl