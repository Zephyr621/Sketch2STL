import cadquery as cq
# --- Part 1: Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1705 * 0.75  # Inner hole radius scaled
height = 0.0312
# Create the washer by making a circle and then cutting out a smaller circle
washer = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(inner_radius)
    .cutBlind(height)
)
# Export the result to a STL file
cq.
# Export the result to a STL file
cq.
# Export the result to a STL file
cq.
# Export the result to a STL file
cq.
# Export the result to a STL file
cq.cq.exporters.export({result_var}, "output_1139.stl"output_1139.stl