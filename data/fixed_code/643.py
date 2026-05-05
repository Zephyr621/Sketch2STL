import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.3125 * 0.75  # Scaled width
height = 0.0167
hole_radius = 0.0158 * 0.75  # Scaled radius
hole1_x = 0.375 * 0.75  # Scaled x-coordinate
hole1_y = 0.1562 * 0.75  # Scaled y-coordinate
hole2_x = 0.575 * 0.75  # Scaled x-coordinate
hole2_y = 0.1562 * 0.75  # Scaled y-coordinate
# --- Create the base rectangular prism ---
rect = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
rect = rect.faces(">Z").workplane().pushPoints([(hole1_x - length/2, hole1_y - width/2)]).hole(2 * hole_radius)
rect = rect.faces(">Z").workplane().pushPoints([(hole2_x - length/2, hole2_y - width/2)]).hole(2 * hole_radius)
# --- Apply translation ---
rect = rect.translate((0, 0, 0.0469))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_643.stl"output_643.stl