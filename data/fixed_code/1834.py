import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3743 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4607 * 0.75)
    .lineTo(0.5357 * 0.75, 0.5577 * 0.75)
    .lineTo(0.2936 * 0.75, 0.4594 * 0.75)
    .lineTo(0.0, 0.4607 * 0.75)
    .close()
    .extrude(0.3854)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3854, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1834.stl"output_1834.stl