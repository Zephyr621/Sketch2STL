import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.045
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Round Edges and Corners ---
edge_radius = 0.05  # Adjust the radius as needed for desired roundness
part_1 = part_1.edges("|Z").fillet(edge_radius)
part_1 = part_1.edges(">Z or <Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_3295.stl