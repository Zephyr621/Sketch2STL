import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.2679 * 0.75  # Scaled width
height = 0.0625
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
# --- Final Result ---
result = part_1
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_3160.stl