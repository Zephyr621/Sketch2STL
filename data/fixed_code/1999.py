import cadquery as cq
from cadquery.vis import show 
# --- Part 1: Cylinder ---
part_1_radius = 0.025 * 0.05  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY")     .circle(part_1_radius)     .extrude(part_1_height)
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
cq.
cq.
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_1999.stl