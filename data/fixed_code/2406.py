import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Sketch length scaled
width = 0.4583 * 0.75  # Sketch width scaled
height = 0.0185
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
cq.cq.exporters.export({result_var}, "output_2406.stl"output_2406.stl