import cadquery as cq
# --- Part 1: Rectangular Object with Rounded Corners ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.3115 * sketch_scale
height = 0.0049
# Define corner radius (scaled)
corner_radius = 0.0274 * sketch_scale  # Radius of the rounded corners
# Create the base rectangle with rounded corners
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .lineTo(0, width - corner_radius)
    .radiusArc((corner_radius, width), -corner_radius)
    .lineTo(length - corner_radius, width)
    .radiusArc((length, width - corner_radius), -corner_radius)
    .lineTo(length, corner_radius)
    .radiusArc((length - corner_radius, 0), -corner_radius)
    .close()
    .extrude(height)
)
# Apply translation
part_1 = part_1.translate((0, 0, 0.0049))
# Export the result to a STL file
cq.cq.exporters.export({result_var}, "output_1423.stl"output_1423.stl