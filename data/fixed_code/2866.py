import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0234 * 0.0469, 0.0)
    .lineTo(0.0234 * 0.0469, 0.0039 * 0.0469)
    .lineTo(0.0, 0.0039 * 0.0469)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2866.stl"output_2866.stl