import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .rect(0.75 * 0.75, 0.4688 * 0.75)
    .extrude(0.2188)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2188, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_495.stl"output_495.stl