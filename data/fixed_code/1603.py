import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.4239)
    .lineTo(0.5156, 0.4239)
    .lineTo(0.5156, 0.2357)
    .lineTo(0.2577, 0.2357)
    .lineTo(0.2577, 0.4688)
    .lineTo(0.0, 0.4688)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1834 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1603.stl"output_1603.stl