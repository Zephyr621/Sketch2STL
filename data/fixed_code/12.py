import cadquery as cq
# --- Part 1: Rectangular Block with Step ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.25 * sketch_scale
height = 0.1875
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0.25 * sketch_scale, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_12.stl"output_12.stl