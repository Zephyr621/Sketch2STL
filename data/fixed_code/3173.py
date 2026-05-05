import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.2454)
    .lineTo(0.5, 0.2454)
    .lineTo(0.5, 0.4687)
    .lineTo(0.25, 0.4687)
    .lineTo(0.25, 0.0484)
    .lineTo(0.0, 0.0484)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0923 + 0.0923)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0923, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_3173.stl"output_3173.stl