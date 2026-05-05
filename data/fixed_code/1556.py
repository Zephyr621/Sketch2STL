import cadquery as cq
# --- Part 1: Cube ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.375 * 0.75, 0.4687 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2562)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2562, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1556.stl"output_1556.stl