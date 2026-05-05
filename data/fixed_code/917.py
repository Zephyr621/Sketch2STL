import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.5357 * 0.75  # Scaled width
height = 0.2143
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2143))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_917.stl"output_917.stl