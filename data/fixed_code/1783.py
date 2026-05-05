import cadquery as cq
# --- Part 1: Rectangular Bar ---
length = 0.75 * 0.75  # Scaled length
width = 0.0625 * 0.75  # Scaled width
height = 0.0056  # Height
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1783.stl"output_1783.stl