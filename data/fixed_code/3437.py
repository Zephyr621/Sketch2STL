import cadquery as cq
# --- Part 1: Rectangular Block with Circular Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.2647 * 0.75  # Scaled width
height = 0.4412
hole_radius = 0.0882 * 0.75  # Scaled radius
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.1324 * 0.75  # Scaled center y
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
# Export to STL
cq.cq.exporters.export({result_var}, "output_3437.stl"output_3437.stl