import cadquery as cq
# --- Part 1: Square Plate with Hole ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.075
hole_radius = 0.0375 * 0.75  # Scaled radius
# Create the base square plate
plate = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# Create the hole
hole = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(plate_height)
    .translate((0,0,plate_height))
)
# Cut the hole from the plate
result = plate.cut(hole)
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_529.stl"output_529.stl