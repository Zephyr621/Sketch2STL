import cadquery as cq
# --- Part 1: Rectangular Box ---
outer_width = 0.75 * 0.75  # Scaled width
outer_length = 0.5354 * 0.75  # Scaled length
inner_offset = 0.0412 * 0.75  # Scaled offset
height = 0.2486
part_1 = (
    cq.Workplane("XY")
    .rect(outer_width, outer_length)
    .extrude(height)
)
inner_box = (
    cq.Workplane("XY")
    .rect(outer_width - 2 * inner_offset, outer_length - 2 * inner_offset)
    .extrude(height)
)
result = part_1.cut(inner_box)
cq.
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_668.stl