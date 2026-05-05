import cadquery as cq
# --- Part 1: Cube ---
length = 0.0182 * 0.75  # Sketch length scaled
width = 0.75 * 0.75   # Sketch width scaled
height = 0.0078
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
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
cq.
cq.cq.exporters.export({result_var}, "output_3166.stl"output_3166.stl