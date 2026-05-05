import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.3842 * 0.5422  # Sketch length scaled
width = 0.5422 * 0.5422  # Sketch width scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
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
# Export to STL
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2514.stl