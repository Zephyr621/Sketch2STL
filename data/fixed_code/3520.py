import cadquery as cq
# --- Part 1: Rectangular Bar ---
length = 0.0059 * 0.0195  # Scaled length
width = 0.0195 * 0.0195   # Scaled width
height = 0.75
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
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_3520.stl