import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.1875
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Add Hole ---
hole_radius = 0.05  # Adjust for desired roundness
part_1 = part_1.faces(">Z").workplane().center(0.375 * 0.75 - (part_1_size/2), 0.375 * 0.75 - (part_1_size/2)).circle(hole_radius).cutThruAll()
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1546.stl"output_1546.stl