import cadquery as cq
# --- Part 1: Rectangular Base ---
outer_rect_size = 0.75 * 0.75  # Scaled size
inner_rect_offset = 0.0268 * 0.75  # Scaled offset
height = 0.0536
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_size, outer_rect_size)
    .extrude(height)
    .faces(">Z").workplane()
    .rect(outer_rect_size - 2 * inner_rect_offset, outer_rect_size - 2 * inner_rect_offset)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_528.stl"output_528.stl