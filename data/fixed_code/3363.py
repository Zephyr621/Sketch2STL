import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.6346 * 0.75, 0.0)
    .lineTo(0.6346 * 0.75, 0.0764 * 0.75)
    .lineTo(0.75 * 0.75, 0.0764 * 0.75)
    .lineTo(0.75 * 0.75, 0.5344 * 0.75)
    .lineTo(0.0, 0.5344 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1215)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1215, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_3363.stl"output_3363.stl