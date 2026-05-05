import cadquery as cq
# --- Part 1: Cylinder with Rectangular Top and Hole ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.45 * sketch_scale
height = 0.15
hole_center_x = 0.225 * sketch_scale
hole_center_y = 0.225 * sketch_scale
hole_radius = 0.075 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(hole_radius)
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
cq.cq.exporters.export({result_var}, "output_527.stl"output_527.stl