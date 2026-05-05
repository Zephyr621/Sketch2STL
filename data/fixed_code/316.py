import cadquery as cq
# --- Part 1: House ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2596 * 0.2624, 0.0)
    .lineTo(0.2624 * 0.2624, 0.1667 * 0.2624)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
# --- Export to STL ---
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_316.stl"output_316.stl