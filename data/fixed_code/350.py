import cadquery as cq
# --- Part 1: Square Plate ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_thickness = 0.0234
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_thickness)
# --- Fillet Edges ---
edge_radius = min(part_1_size / 10, part_1_thickness / 2)  # Adjust as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
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
cq.exporters.export(result, "output_350.stl