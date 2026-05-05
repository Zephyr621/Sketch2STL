import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.5357 * 0.75  # Sketch width scaled
part_1_height = 0.0029
part_1 = cq.Workplane("XY").box(part_1_length, part_1_width, part_1_height)
# --- Round Edges and Corners ---
edge_radius = min(part_1_length, part_1_width, part_1_height) / 10  # Adjust radius as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
part_1 = part_1.edges(">Z or <Z").fillet(edge_radius)
part_1 = part_1.edges("<X or >X or <X").fillet(edge_radius)
part_1 = part_1.edges(">Y or <Y").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1036.stl"output_1036.stl