import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.4412 * 0.75  # Scaled width
height = 0.0156
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0156))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Fillet Edges ---
edge_radius = min(length, width) / 10  # Adjust as needed
assembly = assembly.edges("|Z").fillet(edge_radius)
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2898.stl