import cadquery as cq
from cadquery.vis import show
# --- Part 1: Semi-Cylinder ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.3261 * 0.75), (0.75 * 0.75, 0.5296 * 0.75))
    .lineTo(0.75 * 0.75, 0.6136 * 0.75)
    .threePointArc((0.375 * 0.75, 0.6364 * 0.75), (0.0, 0.6136 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2497)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_2634.stl