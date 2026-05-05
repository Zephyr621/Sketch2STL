import cadquery as cq
# --- Part 1: Trapezoidal Prism ---
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.25 * 0.75 # Scaled height
part_1_depth = 0.0117 * 0.75 # Scaled depth
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3390.stl"output_3390.stl