import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Ring ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.2344 * 0.75
height = 0.1178
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
# Export to STL
# Export to STL
# Export to STL
# Export to STL
exporters.
# 导出为STL文件
cq.exporters.export(result, "output_447.stl