import cadquery as cq
# --- Part 1: Rock ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.3214)
    .lineTo(0.5357, 0.6429)
    .lineTo(0.2143, 0.6429)
    .lineTo(0.2143, 0.4286)
    .lineTo(0.0, 0.4286)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0139 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0238 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1570.stl"output_1570.stl