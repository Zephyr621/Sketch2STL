import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate with Rounded Corners ---
sketch_scale = 0.75
extrude_depth = 0.0214 * sketch_scale
width = 0.5769 * sketch_scale
length = 0.75 * sketch_scale
thickness = 0.0214 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, thickness)
    .threePointArc((thickness, thickness), (0.0044 * sketch_scale, 0.0044 * sketch_scale))
    .lineTo(0.0, thickness)
    .close()
    .extrude(extrude_depth)
)
# Add rounded corners
corner_radius = min(length, thickness) / 10  # Adjust as needed
part_1 = part_1.edges("|Z and >X").fillet(corner_radius)
part_1 = part_1.edges("|Z and <X").fillet(corner_radius)
part_1 = part_1.edges("|Z and >Y").fillet(corner_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2536.stl