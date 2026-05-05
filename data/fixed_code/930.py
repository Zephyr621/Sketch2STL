import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled by sketch_scale
width = 0.375 * 0.75  # Scaled by sketch_scale
height = 0.0375
hole_center_x = 0.375 * 0.75  # Scaled by sketch_scale
hole_center_y = 0.1875 * 0.75  # Scaled by sketch_scale
hole_radius = 0.0225 * 0.75  # Scaled by sketch_scale
# --- Create the rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
plate = plate.faces(">Z").workplane().moveTo(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_930.stl"output_930.stl