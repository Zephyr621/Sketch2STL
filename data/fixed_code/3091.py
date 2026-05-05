import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.5676 * 0.75  # Scaled width
height = 0.1355 * 2  # Total height (both directions)
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2799, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
assembly = assembly.rotate((0, 0, 0), (0, 0, 1), -90)
assembly = assembly.translate((0, 0.1355, 0))
# --- Final Result ---
result = assembly
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3091.stl"output_3091.stl