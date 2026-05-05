import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2027 * sketch_scale
height = 0.0304
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0622 * sketch_scale), (0.75 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.1215 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.2005 * sketch_scale), (0.0, 0.1215 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_1712.stl