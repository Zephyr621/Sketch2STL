import cadquery as cq
from cadquery.vis import show
# --- Part 1: Semi-Cylinder ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.1429 * 0.75), (0.3669 * 0.75, 0.5357 * 0.75))
    .lineTo(0.0, 0.5357 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1071)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1071))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_1342.stl"output_1342.stl