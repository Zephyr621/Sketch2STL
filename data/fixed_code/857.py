import cadquery as cq
# --- Parameters from JSON ---
length = 0.5511 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.1
hole_x = 0.0938 * 0.75  # Scaled hole x
hole_y = 0.1862 * 0.75  # Scaled hole y
hole_size = (0.5469 - 0.0938) * 0.75  # Scaled hole size
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
block = block.faces(">Z").workplane().moveTo(hole_x - length/2, hole_y - width/2).circle(hole_size).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_857.stl"output_857.stl