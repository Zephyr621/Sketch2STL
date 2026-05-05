import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0117 * 0.0333  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Hole ---
hole_radius = 0.0072 * 0.01  # Sketch radius scaled
hole_depth = 0.25
hole = cq.Workplane("XY").circle(hole_radius).extrude(-hole_depth)
# --- Coordinate System Transformation for Hole ---
hole = hole.rotate((0, 0, 0), (1, 0, 0), -90)
hole = hole.rotate((0, 0, 0), (0, 0, 1), -90)
hole = hole.translate((0.375, 0, 0))
# --- Assembly ---
assembly = part_1.cut(hole)
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_2437.stl"output_2437.stl