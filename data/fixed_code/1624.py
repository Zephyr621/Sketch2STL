import cadquery as cq
# --- Part 1: Square Ring ---
outer_size = 0.75 * 0.75  # Scaled outer size
inner_offset = 0.0036 * 0.75  # Scaled inner offset
height = 0.0214
part_1 = (
    cq.Workplane("XY")
    .rect(outer_size, outer_size)
    .extrude(height)
    .cut(cq.Workplane("XY").rect(outer_size - 2 * inner_offset, outer_size - 2 * inner_offset).extrude(height))
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
cq.cq.exporters.export({result_var}, "output_1624.stl"output_1624.stl