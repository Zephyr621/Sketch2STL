import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.125
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Rounding Edges (Slight Curvature) ---
edge_radius = min(part_1_length, part_1_width, part_1_height) / 10  # Adjust radius as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
part_1 = part_1.edges(">Z").fillet(edge_radius)
part_1 = part_1.edges("<Z").fillet(edge_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.125, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1366.stl