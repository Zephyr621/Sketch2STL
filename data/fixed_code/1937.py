import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0857 * 0.1714  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.0828 * 0.1714  # Sketch radius scaled
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.0289)  # Move to the top face of part_1
    .moveTo(0.0429, 0.0429)  # Translate to the center of part_1
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude downwards for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0078, 0.0078, part_1_height))
# --- Assembly ---
result = part_1.cut(part_2)
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_1937.stl"output_1937.stl