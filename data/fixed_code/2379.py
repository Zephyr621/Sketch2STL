import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3634 * 0.75)
    .lineTo(0.0, 0.3634 * 0.75)
    .close()
    .extrude(-0.0314)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2379.stl"output_2379.stl