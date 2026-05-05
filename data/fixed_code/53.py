import cadquery as cq
# --- Part 1: Triangle Prism ---
sketch_scale = 0.75
extrude_depth = 0.0469 * sketch_scale
# Define the points for the triangle vertices (scaled)
points = [
    (0.0 * sketch_scale, 0.0 * sketch_scale),
    (0.3188 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.4375 * sketch_scale),
    (0.4375 * sketch_scale, 0.5 * sketch_scale),
    (0.0 * sketch_scale, 0.5531 * sketch_scale)
]
# Create the solid using CQ
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
# Export to STL
cq.
cq.
cq.exporters
# 导出为STL文件
cq.exporters.export(result, "output_53.stl