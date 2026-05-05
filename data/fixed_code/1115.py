import cadquery as cq
# --- Part 1: S-shaped Object ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7194 * 0.75, 0.0)
    .lineTo(0.7194 * 0.75, 0.1739 * 0.75)
    .lineTo(0.75 * 0.75, 0.1739 * 0.75)
    .lineTo(0.75 * 0.75, 0.5055 * 0.75)
    .lineTo(0.3752 * 0.75, 0.5055 * 0.75)
    .lineTo(0.3752 * 0.75, 0.4362 * 0.75)
    .lineTo(0.0, 0.4362 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4286)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4286, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_1115.stl"output_1115.stl