import cadquery as cq
# --- Part 1: Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1714 * 0.75  # Inner hole radius scaled
height = 0.0536
# Create the washer by making a cylinder and then cutting out a smaller cylinder
washer = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_254.stl"output_254.stl