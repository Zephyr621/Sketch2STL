import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1818)
    .lineTo(0.5625, 0.4187)
    .lineTo(0.1818, 0.4187)
    .lineTo(0.1818, 0.1818)
    .lineTo(0.0, 0.1818)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2882)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2882, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3222.stl"output_3222.stl