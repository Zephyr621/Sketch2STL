import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius_outer = 0.075 * 0.15  # Sketch radius scaled
part_1_radius_inner = 0.03 * 0.15
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_radius_outer)
    .circle(part_1_radius_inner)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2076.stl"output_2076.stl