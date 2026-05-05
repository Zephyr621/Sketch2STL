import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.625 * 0.75  # Scaled width
height = 0.5
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Apply rotation and translation ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
part_1 = part_1.edges(">Z or <Z or |X or |Y").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1656.stl