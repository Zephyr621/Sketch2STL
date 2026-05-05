import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1543)
    .threePointArc((0.7061, 0.5391), (0.5309, 0.4152))
    .lineTo(0.1667, 0.4152)
    .threePointArc((0.0071, 0.2335), (0.0, 0.1543))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3728)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3728, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2459.stl"output_2459.stl