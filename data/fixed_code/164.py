import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.3385 * 0.75  # Scaled width
height = 0.2163
part_1 = cq.Workplane("XY").rect(length, width).extrude(-height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_164.stl"output_164.stl