import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0375 * 0.0375  # Sketch width scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_width).extrude(part_1_height)
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
cq.
cq.cq.exporters.export({result_var}, "output_3305.stl"output_3305.stl