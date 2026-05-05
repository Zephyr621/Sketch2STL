import cadquery as cq
# --- Part 1: Disk Disc ---
sketch_scale = 0.75
radius = 0.375 * sketch_scale
depth = 0.0417
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1562 * sketch_scale, 0.375 * sketch_scale)
    .circle(radius)
    .moveTo(0.3125 * sketch_scale, 0.6125 * sketch_scale)
    .circle(radius)
    .extrude(-depth)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_1765.stl"output_1765.stl