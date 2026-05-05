import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7188 * 0.75, 0.0)
    .lineTo(0.7188 * 0.75, 0.5192 * 0.75)
    .lineTo(0.4203 * 0.75, 0.5192 * 0.75)
    .lineTo(0.4203 * 0.75, 0.6218 * 0.75)
    .lineTo(0.0, 0.6218 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4091)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4091, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_2140.stl"output_2140.stl