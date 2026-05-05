import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.225
hole_center_x = 0.1125 * 0.75  # Scaled center x
hole_center_y = 0.1875 * 0.75  # Scaled center y
hole_radius = 0.0562 * 0.75  # Scaled radius
# --- Create the rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
block = block.faces(">Z").workplane().moveTo(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2390.stl"output_2390.stl