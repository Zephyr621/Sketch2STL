import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0193 * 0.2357, 0.0)
    .lineTo(0.0193 * 0.2357, 0.1154 * 0.2357)
    .lineTo(0.0017 * 0.2357, 0.1154 * 0.2357)
    .lineTo(0.0017 * 0.2357, 0.0)
    .lineTo(0.0193 * 0.2357, 0.0)
    .lineTo(0.0193 * 0.2357, 0.2357 * 0.2357)
    .lineTo(0.0, 0.2357 * 0.2357)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
#part_1 = part_1.translate((0, 0, 0)) # Translation not needed
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3058.stl"output_3058.stl