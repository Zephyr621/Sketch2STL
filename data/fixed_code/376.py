import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.15
hole_radius = 0.0375 * 0.75  # Scaled radius
mounting_hole_radius = 0.0225 * 0.75  # Scaled radius
center_hole_offset = 0.075 * 0.75  # Scaled offset
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the central hole ---
block = block.faces(">Z").workplane().hole(2 * hole_radius)
# --- Create the mounting holes ---
block = (
    block.faces(">Z")
    .workplane()
    .pushPoints([
        (mounting_hole_offset - length / 2, mounting_hole_offset - width / 2),
        (mounting_hole_offset - length / 2, center_hole_offset - width / 2),
    ])
    .hole(2 * mounting_hole_radius)
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_376.stl"output_376.stl