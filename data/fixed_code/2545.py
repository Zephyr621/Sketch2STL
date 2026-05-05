import cadquery as cq
# --- Part 1: Square Frame ---
outer_size = 0.75 * 0.75  # Scaled outer dimension
inner_offset = 0.0112 * 0.75  # Scaled inner offset
frame_height = 0.0225
outer_square = cq.Workplane("XY").rect(outer_size, outer_size).extrude(frame_height)
inner_square = cq.Workplane("XY").rect(outer_size - 2 * inner_offset, outer_size - 2 * inner_offset).extrude(frame_height)
part_1 = outer_square.cut(inner_square)
# --- Final Result ---
result = part_1
cq.
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2545.stl"output_2545.stl