import cadquery as cq
# --- Part 1: Circular Plate with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.0625 * 0.75  # Sketch radius scaled for the hole
plate_height = 0.0375
wp = cq.Workplane("XY").circle(outer_radius).extrude(plate_height)
hole = cq.Workplane("XY").circle(inner_radius).extrude(plate_height)
part_1 = wp.cut(hole)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0375, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1782.stl"output_1782.stl