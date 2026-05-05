import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.3782 * 0.75  # Scaled width
height = 0.2452
inner_length = 0.6136 * 0.75
inner_width = 0.3722 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
inner_box = (
    cq.Workplane("XY")
    .rect(inner_length, inner_width)
    .extrude(height)
)
part_1 = part_1.cut(inner_box)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_972.stl