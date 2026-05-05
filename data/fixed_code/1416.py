import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.625 * 0.75  # Scaled width
height = 0.5
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
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
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_1416.stl