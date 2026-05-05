import cadquery as cq
# --- Part 1: Vertical Line Segment ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0769 * 0.75)
    .lineTo(0.3106 * 0.75, 0.0769 * 0.75)
    .lineTo(0.1587 * 0.75, 0.0769 * 0.75)
    .threePointArc((0.375 * 0.75, 0.0), (0.5104 * 0.75, 0.0769 * 0.75))
    .lineTo(0.5944 * 0.75, 0.0769 * 0.75)
    .threePointArc((0.6311 * 0.75, 0.0), (0.6119 * 0.75, 0.0769 * 0.75))
    .lineTo(0.6119 * 0.75, 0.0769 * 0.75)
    .lineTo(0.0, 0.0769 * 0.75)
    .close()
    .extrude(0.0134)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_3580.stl"output_3580.stl