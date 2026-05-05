import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.7036  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.3571 * 0.7036  # Sketch radius scaled
part_2_height = 0.3125
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0026, 0.0, 0.0026))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final Result ---
result = assembly
cq.
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_470.stl