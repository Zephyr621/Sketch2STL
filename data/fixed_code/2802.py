import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.3 * 0.75  # Scaled width
height = 0.15
inner_length = (0.7083 - 0.0208) * 0.75
inner_width = (0.3962 - 0.1133) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .cut(cq.Workplane("XY").rect(inner_length, inner_width).extrude(height))
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2802.stl