import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.1875 * 0.5625  # Scaled length
width = 0.5625 * 0.5625   # Scaled width
height = 0.0375
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0375))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1097.stl"output_1097.stl