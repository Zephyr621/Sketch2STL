import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.15 * 0.75   # Scaled width
height = 0.1875 + 0.1875  # Total height (both directions)
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Apply fillets to edges ---
edge_radius = min(length, width) / 10  # Adjust radius as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
result = result.rotate((0, 0, 0), (0, 0, 1), -90)
result = result.translate((0, 0.375, 0
# 导出为STL文件
cq.exporters.export(result, "output_65.stl