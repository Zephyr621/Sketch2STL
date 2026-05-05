import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.0536 * 0.1071  # Sketch radius scaled
part_1_height = 0.0536
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Hole ---
hole_radius = 0.0082 * 0.0114  # Sketch radius scaled
hole_depth = 0.0469
part_2 = cq.Workplane("XY").circle(hole_radius).extrude(-hole_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0536, 0.3386, 0.0536))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.cq.exporters.export({result_var}, "output_2882.stl"output_2882.stl