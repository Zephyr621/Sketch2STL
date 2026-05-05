import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0312
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Cut Cylinders ---
sketch_scale = 0.625
cylinder_radius = 0.3125 * sketch_scale
cut_depth = 0.0313
# Cylinder positions (scaled)
cylinder_positions = [
    (0.1562 + 0.3125)/2,  # Adjusted for center at given points
    (0.1562 + 0.4125)/2,  # Adjusted for center at given points
    (0.1562 + 0.6125)/2,  # Adjusted for center at given points
]
# Create cylinders
for x, y in cylinder_positions:
    cylinder = cq.Workplane("XY").moveTo(x - 0.375/2, y - 0.375/2).circle(cylinder_radius).extrude(-cut_depth)
    part_1 = part_1.translate((0, 0, part_1_height))
# --- Assembly ---
result = part_1.cut(cylinder)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_2530.stl"output_2530.stl