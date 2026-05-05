import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0741 * 0.0955  # Sketch width scaled
part_1_length = 0.0955 * 0.0955 # Sketch length scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_length).extrude(part_1_height)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_2956.stl