import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.2945 * 0.5848  # Sketch radius scaled
inner_radius = 0.1625 * 0.5848  # Inner radius scaled
height = 0.75
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
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1454.stl"output_1454.stl