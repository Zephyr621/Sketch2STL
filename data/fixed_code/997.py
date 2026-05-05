import cadquery as cq
# --- Part 1: Cylinder with a hole ---
outer_radius = 0.2679 * 0.5357  # Sketch radius scaled
inner_radius = 0.1071 * 0.5357  # Inner radius for the hole, scaled
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
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_997.stl"output_997.stl