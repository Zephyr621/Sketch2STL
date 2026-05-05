import cadquery as cq
# --- Part 1: Shield ---
sketch_scale = 0.75
extrude_depth = 0.0816 * sketch_scale
# Scaled dimensions
width = 0.5357 * sketch_scale
height = 0.5714 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(width, 0)
    .lineTo(width, height)
    .lineTo(0, height)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0816 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3403.stl"output_3403.stl