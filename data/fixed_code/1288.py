import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3281 * 0.75)
    .lineTo(0.2166 * 0.75, 0.0)
    .lineTo(0.4167 * 0.75, 0.1849 * 0.75)
    .lineTo(0.4167 * 0.75, 0.5625 * 0.75)
    .lineTo(0.1982 * 0.75, 0.5625 * 0.75)
    .lineTo(0.0, 0.3281 * 0.75)
    .close()
    .extrude(0.1612)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0643, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1288.stl"output_1288.stl