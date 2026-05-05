import cadquery as cq
# --- Part 1: Cube with Hollow Center ---
outer_width = 0.4286 * 0.4286  # Scaled width
outer_length = 0.4286 * 0.4286 # Scaled length
inner_offset = 0.0105 * 0.4286 # Scaled offset for inner square
height = 0.75
# Create the outer cube
outer_cube = cq.Workplane("XY").rect(outer_width, outer_length).extrude(height)
# Create the inner square (to be cut out)
inner_cube = cq.Workplane("XY").rect(outer_width - 2 * inner_offset, outer_length - 2 * inner_offset).extrude(height)
# Cut the inner cube from the outer cube
part_1 = outer_cube.cut(inner_cube)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3120.stl"output_3120.stl