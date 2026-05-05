import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Bar ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0769 * 0.75  # Scaled width
part_1_height = 0.0577
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0577, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.3345 * 0.6793  # Scaled radius
part_2_depth = 0.0577
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0196, 0, 0.0196))
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_1298.stl"output_1298.stl