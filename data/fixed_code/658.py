import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.25 * 0.75   # Scaled width
height = 0.0156
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0156))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Apply translation to the assembly ---
assembly = assembly.translate((0, 0, 0.0156))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_658.stl"output_658.stl