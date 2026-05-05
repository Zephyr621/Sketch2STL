import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.3214 * 0.75  # Scaled width
height = 0.0057
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
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
# Export to STL
cq.
cq.exporters.
# 导出为STL文件
cq.exporters.export(result, "output_494.stl