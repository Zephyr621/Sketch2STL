import cadquery as cq
from cadquery.vis import show
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.75
height = 0.2679
# Scaled coordinates for the hexagon vertices
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.3248 * sketch_scale, 0.0 * sketch_scale),
    (0.6495 * sketch_scale, 0.0 * sketch_scale),
    (0.6495 * sketch_scale, 0.3248 * sketch_scale)
]
# Extrusion depth
extrude_depth = 0.2679
# Create the hexagonal base
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export
# 导出为STL文件
cq.exporters.export(result, "output_2919.stl