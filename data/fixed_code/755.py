import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hollow Interior ---
outer_radius = 0.2679 * 0.5357  # Sketch radius scaled
inner_radius = 0.1071 * 0.5357  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_755.stl"output_755.stl