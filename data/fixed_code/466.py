import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4687 * 0.4687, 0.0)
    .lineTo(0.4687 * 0.4687, 0.0188 * 0.4687)
    .threePointArc((0.2344 * 0.4687, 0.0013 * 0.4687), (0.0234 * 0.4687, 0.0188 * 0.4687))
    .lineTo(0.0234 * 0.4687, 0.0033 * 0.4687)
    .lineTo(0.0, 0.0033 * 0.4687)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_466.stl"output_466.stl