import cadquery as cq
# --- Part 1: Triangular Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3237 * 0.75)  # Scale sketch
    .lineTo(0.0484 * 0.75, 0.0)  # Scale sketch
    .lineTo(0.7344 * 0.75, 0.4203 * 0.75)  # Scale sketch
    .lineTo(0.6173 * 0.75, 0.4822 * 0.75)  # Scale sketch
    .lineTo(0.0, 0.3237 * 0.75)  # Scale sketch
    .close()
    .extrude(0.0125)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0125, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.cq.exporters.export({result_var}, "output_288.stl"output_288.stl