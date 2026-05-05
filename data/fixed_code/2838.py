import cadquery as cq
from cadquery.vis import show 
# --- Part 1: Triangle Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)  # Scale the sketch
    .lineTo(0.375 * 0.75, 0.0)  # Scale the sketch
    .lineTo(0.375 * 0.75, 0.75 * 0.75)  # Scale the sketch
    .lineTo(0.0, 0.0)  # Scale the sketch
    .close()  # Extrude depth
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
cq.
cq.
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2838.stl