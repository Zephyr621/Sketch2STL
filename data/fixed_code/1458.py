import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.5417 * 0.75  # Scaled width
height = 0.0151
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0151))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Fillet the corners ---
corner_radius = min(length, width) / 10  # Adjust as needed
assembly = assembly.edges("|Z and >X").fillet(corner_radius)
assembly = assembly.edges("|Z and <X").fillet(corner_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1458.stl