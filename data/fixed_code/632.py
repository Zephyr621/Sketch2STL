import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangular Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.5714 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1816 + 0.1816)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.cq.exporters.export({result_var}, "output_632.stl"output_632.stl