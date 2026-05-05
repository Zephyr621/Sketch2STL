import cadquery as cq
from math import radians
# --- Part 1: Base Rectangle ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6198 * 0.75  # Scaled width
part_1_height = 0.1897
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Circular Hole ---
part_2_radius = 0.1451 * 0.2804  # Scaled radius
part_2_depth = 0.2737
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.375, 0.3261, 0.1897))
# --- Assembly: Cut the hole from the base ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq
# 导出为STL文件
cq.exporters.export(result, "output_3159.stl