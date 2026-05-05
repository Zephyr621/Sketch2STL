import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_size = 0.75 * 0.75  # Scaled outer square size
inner_radius = 0.1875 * 0.75  # Scaled inner circle radius
height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(outer_size, outer_size)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2256.stl"output_2256.stl