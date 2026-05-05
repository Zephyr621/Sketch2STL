import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.0268 * 0.75  # Scaled width
height = 0.0029 * 2  # Total height (both directions)
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0268, 0))
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
# --- Apply translation to the assembly ---
assembly = assembly.translate((0, 0, 0.0134))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1684.stl"output_1684.stl