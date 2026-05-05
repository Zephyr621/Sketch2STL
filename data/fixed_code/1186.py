import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.2469 * 0.75  # Scaled width
height = 0.1875
# Create the first rectangle
rect1_length = (0.4972 - 0.1223) * 0.75
rect1_width = (0.2577 - 0.1223) * 0.75
# Create the second rectangle
rect2_length = (0.2469 - 0.1223) * 0.75
rect2_width = (0.2469 - 0.1223) * 0.75
# Extrude the combined shape
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Apply rotation
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Apply translation
part_1 = part_1.translate((0, 0.375, 0))
# Export the result to a STL file
cq.
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_1186.stl"output_1186.stl