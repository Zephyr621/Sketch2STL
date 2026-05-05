import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.1154 * 0.1154  # Sketch length scaled
part_1_width = 0.0833 * 0.1154  # Sketch width scaled
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, part_1_width)
    .lineTo(part_1_length, part_1_width)
    .lineTo(part_1_length / 2, 0)
    .lineTo(part_1_length / 2, part_1_width)
    .close()
    .extrude(part_1_height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_2553.stl"output_2553.stl