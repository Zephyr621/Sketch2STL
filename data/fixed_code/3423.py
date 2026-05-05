import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4091 * 0.75  # Scaled width
height = 0.3107
hole_radius = 0.0536 * 0.75  # Scaled radius
hole_center1 = (0.1034 * 0.75 - length/2, 0.1034 * 0.75 - width/2)  # Scaled center
hole_center2 = (0.6409 * 0.75 - length/2, 0.1034 * 0.75 - width/2)  # Scaled center
# --- Create the base rectangular prism ---
rect = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
rect = rect.faces(">Z").workplane().pushPoints([hole_center1]).hole(2 * hole_radius)
rect = rect.faces(">Z").workplane().pushPoints([hole_center2]).hole(2 * hole_radius)
# --- Apply rotation and translation ---
rect = rect.rotate((0, 0, 0), (0, 0, 1), -90)
rect = rect.translate((0, 0.3107, 0))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_3423.stl"output_3423.stl