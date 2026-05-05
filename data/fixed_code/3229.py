import cadquery as cq
# --- Part 1: Cube ---
side_length = 0.7495 * 0.7495  # Sketch side length scaled
cube = cq.Workplane("XY").box(side_length, side_length, side_length)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = cube
cq.
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
cq.exporters.export(result, "output_3229.stl