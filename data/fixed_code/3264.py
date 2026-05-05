import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.4643 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0071 * 2  # Total height (both directions)
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0107))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
cq.cq.exporters.export({result_var}, "output_3264.stl"output_3264.stl