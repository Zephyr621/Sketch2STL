import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.1406 * 0.285  # Sketch radius scaled
part_1_height = 0.0268 + 0.0268
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0962, 0.0962, 0))
# --- Part 2: Cylinder (Join) ---
part_2_radius = 0.0134 * 0.0346  # Sketch radius scaled
part_2_height = 0.1172 + 0.1172
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0081, 0.0533, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final Result ---
result = assembly
cq.
cq
# 导出为STL文件
cq.exporters.export(result, "output_1762.stl