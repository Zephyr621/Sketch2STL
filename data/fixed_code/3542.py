import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.4375 * 0.75  # Scaled width
height = 0.0062
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Apply translation ---
part_1 = part_1.translate((0, 0, 0.0062))
# --- Fillet Edges ---
edge_radius = min(length, width) / 10  # Adjust as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3542.stl