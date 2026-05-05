import cadquery as cq
# --- Part 1: Triangle ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1071 * 0.75)
    .lineTo(0.6259 * 0.75, 0.4113 * 0.75)
    .lineTo(0.1132 * 0.75, 0.4113 * 0.75)
    .lineTo(0.0, 0.1071 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3136)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3136, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2639.stl"output_2639.stl