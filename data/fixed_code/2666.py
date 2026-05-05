import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1875)
    .lineTo(0.5156, 0.4125)
    .lineTo(0.3125, 0.4125)
    .lineTo(0.0, 0.4125)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4125)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4125, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2666.stl"output_2666.stl