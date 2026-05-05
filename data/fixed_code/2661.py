import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.25)
    .threePointArc((0.7375, 0.25), (0.625, 0.625))
    .lineTo(0.5, 0.625)
    .threePointArc((0.25, 0.25), (0.0, 0.25))
    .close()
    .extrude(0.25)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2661.stl"output_2661.stl