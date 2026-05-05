import cadquery as cq
# --- Part 1: Cube ---
side_length = 0.75 * 0.75  # Sketch side length scaled
extrusion_depth = 0.0125
part_1 = cq.Workplane("XY").rect(side_length, side_length).extrude(extrusion_depth)
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
cq.cq.exporters.export({result_var}, "output_250.stl"output_250.stl