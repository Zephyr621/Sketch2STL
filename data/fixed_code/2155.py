import cadquery as cq
# --- Part 1: Rectangular Block with Circular Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.1875
hole_center_x = 0.375 * 0.75  # Scaled hole center x
hole_center_y = 0.1875 * 0.75  # Scaled hole center y
hole_radius = 0.0937 * 0.75  # Scaled hole radius
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - length/2, hole_center_y - width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_2155.stl"output_2155.stl