import cadquery as cq
# --- Part 1: Cube with Opening ---
cube_size = 0.75 * 0.75  # Scaled size
cube_height = 0.7387
part_1 = cq.Workplane("XY").box(cube_size, cube_size, cube_height)
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
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2985.stl