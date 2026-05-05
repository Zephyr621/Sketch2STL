import cadquery as cq
# --- Part 1: Torus ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3125 * 0.75
height = 0.0625
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2153.stl"output_2153.stl