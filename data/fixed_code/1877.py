import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.6911 * 0.6893, 0.0)
    .lineTo(0.6911 * 0.6893, 0.3429 * 0.6893)
    .lineTo(0.0417 * 0.6893, 0.3429 * 0.6893)
    .lineTo(0.0417 * 0.6893, 0.6084 * 0.6893)
    .lineTo(0.0632 * 0.6893, 0.6084 * 0.6893)
    .lineTo(0.0632 * 0.6893, 0.3214 * 0.6893)
    .lineTo(0.0417 * 0.6893, 0.3214 * 0.6893)
    .lineTo(0.0417 * 0.6893, 0.6893 * 0.6893)
    .lineTo(0.0, 0.6893 * 0.6893)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1877.stl"output_1877.stl