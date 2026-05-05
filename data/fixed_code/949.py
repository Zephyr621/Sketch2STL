import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.5625 * 0.75  # Scaled width
height = 0.0112
hole_radius = 0.0562 * 0.75  # Scaled radius
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.2812 * 0.75  # Scaled center y
# --- Create the rectangular plate ---
plate = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Create the circular hole ---
plate = plate.faces(">Z").workplane().moveTo(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Apply rotation and translation ---
plate = plate.rotate((0, 0, 0), (0, 0, 1), -90)
plate = plate.translate((0, 0.0112, 0))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_949.stl"output_949.stl