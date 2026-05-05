import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.5294 * 0.75  # Scaled width
height = 0.0146
hole_x_start = 0.1458 * 0.75  # Scaled hole start x
hole_y_start = 0.2519 * 0.75  # Scaled hole start y
hole_x_end = 0.5714 * 0.75  # Scaled hole end x
hole_y_end = 0.5294 * 0.75  # Scaled hole end y
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
hole = (
    cq.Workplane("XY")
    .moveTo(hole_x_start, hole_y_start)
    .lineTo(hole_x_end, hole_y_start)
    .lineTo(hole_x_end, hole_y_end)
    .close()
    .extrude(height + 0.001)  # Extrude slightly more than the plate height
)
# --- Subtract the hole from the plate ---
plate = plate.cut(hole)
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_419.stl"output_419.stl