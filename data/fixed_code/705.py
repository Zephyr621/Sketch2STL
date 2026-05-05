import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0234 * 0.0937, 0.0)
    .lineTo(0.0234 * 0.0937, 0.0937 * 0.0937)
    .lineTo(0.0117 * 0.0937, 0.0937 * 0.0937)
    .lineTo(0.0117 * 0.0937, 0.0469 * 0.0937)
    .lineTo(0.0234 * 0.0937, 0.0469 * 0.0937)
    .lineTo(0.0234 * 0.0937, 0.0469 * 0.0937)
    .lineTo(0.0234 * 0.0937, 0.0469 * 0.0937)
    .lineTo(0.0, 0.0469 * 0.0937)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_705.stl"output_705.stl