import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75   # Scaled width
height = 0.0056
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Apply rotation and translation ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0056, 0))
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
cq.
cq.
cq.
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1472.stl