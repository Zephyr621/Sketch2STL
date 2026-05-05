import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0938 * 0.1807)
    .lineTo(0.0908 * 0.1807, 0.0938 * 0.1807)
    .lineTo(0.0908 * 0.1807, 0.0)
    .lineTo(0.1807 * 0.1807, 0.0)
    .lineTo(0.1807 * 0.1807, 0.0938 * 0.1807)
    .close()
    .extrude(0.1875)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1351.stl"output_1351.stl