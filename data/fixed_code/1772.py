import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2083
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Smaller Cylinder on Top ---
part_2_radius = 0.2583 * 0.5167  # Sketch radius scaled
part_2_height = 0.2917
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1167, 0.1167, 0.2083))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1772.stl