import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.0273 * 0.0421  # Sketch length scaled
part_1_width = 0.0421 * 0.0421   # Sketch width scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.exporters.
# 导出为STL文件
cq.exporters.export(result, "output_2785.stl