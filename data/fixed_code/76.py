import cadquery as cq
# --- Parameters from JSON ---
length = 0.7159
width = 0.75
height = 0.0273
sketch_scale = 0.75
hole_radius = 0.0086 * sketch_scale
center_x1 = 0.3253 * sketch_scale
center_y1 = 0.375 * sketch_scale
center_x2 = 0.3945 * sketch_scale
center_y2 = 0.5342 * sketch_scale
center_x3 = 0.6151 * sketch_scale
center_y3 = 0.5625 * sketch_scale
# --- Create the base plate ---
plate = (
    cq.Workplane("XY")
    .rect(length * sketch_scale, width * sketch_scale)
    .extrude(height)
)
# --- Add the central hole ---
plate = plate.faces(">Z").workplane().pushPoints([(center_x1 - (length * sketch_scale)/2, center_y1 - (width * sketch_scale)/2)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_76.stl"output_76.stl