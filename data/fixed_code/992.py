import cadquery as cq
# --- Parameters from JSON ---
outer_size = 0.75 * 0.75  # Scaled size
inner_offset = 0.0234 * 0.75  # Scaled offset for inner square
frame_height = 0.4688
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(outer_size, outer_size).extrude(frame_height)
# --- Create the inner square (to be cut out) ---
plate = plate.cut(cq.Workplane("XY").rect(outer_size - 2*inner_offset, outer_size - 2*inner_offset).extrude(frame_height))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_992.stl"output_992.stl