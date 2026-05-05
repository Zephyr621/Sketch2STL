import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.2679 * 0.5661  # Scaled length
width = 0.5661 * 0.5661  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
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
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1362.stl