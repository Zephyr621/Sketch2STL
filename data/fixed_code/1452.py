import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1607)
    .lineTo(0.5893, 0.4154)
    .lineTo(0.5114, 0.4154)
    .lineTo(0.5114, 0.1607)
    .lineTo(0.2143, 0.1607)
    .lineTo(0.2143, 0.4415)
    .lineTo(0.0, 0.4415)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0905 + 0.0905)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1885, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_1452.stl"output_1452.stl