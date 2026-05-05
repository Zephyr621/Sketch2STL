import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0188 * 0.75)
    .threePointArc((0.375 * 0.75, 0.0), (0.7188 * 0.75, 0.0188 * 0.75))
    .lineTo(0.7188 * 0.75, 0.0281 * 0.75)
    .threePointArc((0.375 * 0.75, 0.0312 * 0.75), (0.0, 0.0281 * 0.75))
    .lineTo(0.0, 0.0188 * 0.75)
    .close()
    .extrude(0.0056 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0056 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2172.stl"output_2172.stl