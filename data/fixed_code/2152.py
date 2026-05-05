import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0833 * 0.75)
    .lineTo(0.4286 * 0.75, 0.0833 * 0.75)
    .lineTo(0.4286 * 0.75, 0.2143 * 0.75)
    .lineTo(0.2812 * 0.75, 0.2143 * 0.75)
    .lineTo(0.2812 * 0.75, 0.4286 * 0.75)
    .lineTo(0.0, 0.4286 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0154)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2152.stl"output_2152.stl