import cadquery as cq
from cadquery.vis import show
# --- Part 1: Pentagonal Prism ---
part_1_points = [
    (0.0, 0.2235 * 0.75),
    (0.375 * 0.75, 0.0),
    (0.75 * 0.75, 0.4245 * 0.75),
    (0.375 * 0.75, 0.7498 * 0.75)
]
part_1_height = 0.0632
part_1 = (
    cq.Workplane("XY")
    .polyline(part_1_points)
    .close()
    .extrude(part_1_height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_619.stl