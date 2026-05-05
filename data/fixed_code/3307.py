import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.4773)
    .lineTo(0.7143, 0.4773)
    .lineTo(0.7143, 0.4497)
    .lineTo(0.3184, 0.4497)
    .lineTo(0.3184, 0.4319)
    .lineTo(0.0703, 0.4319)
    .lineTo(0.0703, 0.4497)
    .lineTo(0.0, 0.4497)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3214 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3214 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_3307.stl"output_3307.stl