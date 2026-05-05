import cadquery as cq
# --- Part 1: Hexagonal Cylinder ---
sketch_scale = 0.75
height = 0.15
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.1875 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.1875 * sketch_scale),
    (0.5625 * sketch_scale, 0.5625 * sketch_scale)
]
# Create the hexagonal base
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1574.stl