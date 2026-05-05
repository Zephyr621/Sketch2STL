import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0079 * 0.75)
    .lineTo(0.0446 * 0.75, 0.0)
    .lineTo(0.7188 * 0.75, 0.0)
    .threePointArc((0.7363 * 0.75, 0.1247 * 0.75), (0.7188 * 0.75, 0.4332 * 0.75))
    .lineTo(0.0, 0.4219 * 0.75)
    .lineTo(0.0, 0.0079 * 0.75)
    .close()
    .extrude(0.1579)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1579, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2322.stl"output_2322.stl