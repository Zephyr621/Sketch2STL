import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1406)
    .lineTo(0.5625, 0.1406)
    .lineTo(0.5625, 0.4687)
    .lineTo(0.1875, 0.4687)
    .lineTo(0.1875, 0.1406)
    .lineTo(0.0, 0.1406)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0151 + 0.0151)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0151, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2726.stl"output_2726.stl