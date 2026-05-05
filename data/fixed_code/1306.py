import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.75
points = [
    (0.0, 0.1875),
    (0.3248, 0.0),
    (0.6495, 0.1875),
    (0.6495, 0.5625),
    (0.3248, 0.75),
    (0.0, 0.5625)
]
scaled_points = [(x * sketch_scale, y * sketch_scale) for x, y in points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_points)
    .close()
    .extrude(0.2537)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq
# 导出为STL文件
cq.exporters.export(result, "output_1306.stl