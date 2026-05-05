import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.3301 * 0.75), (0.7083 * 0.75, 0.1795 * 0.75))
    .lineTo(0.6702 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.3273 * 0.75), (0.0, 0.3546 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0547)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3176.stl"output_3176.stl