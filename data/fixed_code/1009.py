import cadquery as cq
# --- Part 1: Cube with Corner Cut Off ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.5519 * 0.5519, 0.0)
    .lineTo(0.5519 * 0.5519, 0.5519 * 0.5519)
    .lineTo(0.0, 0.5519 * 0.5519)
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
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1009.stl"output_1009.stl