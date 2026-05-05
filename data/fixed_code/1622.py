import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.7284 * 0.75  # Sketch length scaled
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.5
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Circular Cutout ---
part_2_radius = 0.2344 * 0.4688  # Sketch radius scaled
part_2_depth = 0.5
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.1167 * 0.4688, 0.1167 * 0.4688)  # Translation Vector
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0237, 0, 0))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_1622.stl"output_1622.stl