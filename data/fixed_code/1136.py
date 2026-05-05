import cadquery as cq
# --- Part 1: Triangle Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)  # Scale the sketch
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)  # Scale the sketch
    .lineTo(0.0, 0.4687 * 0.75)  # Scale the sketch
    .close()
    .extrude(0.1191)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1191, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1136.stl"output_1136.stl