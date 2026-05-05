import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2113 * sketch_scale
height = 0.0319
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + (0.7341 - 0.0239), 0.0182), (length/2, width))
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_2132.stl