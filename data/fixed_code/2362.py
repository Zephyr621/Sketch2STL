import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.2812 * 0.75  # Scaled width
height = 0.0938
part_1 = cq.Workplane("XY").rect(length, width).extrude(-height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Fillet Edges ---
edge_radius = min(length, width, height) / 10  # Adjust as needed
part_1 = part_1.edges("|Z").fillet(edge_radius)
part_1 = part_1.edges("<Z").fillet(edge_radius)
part_1 = part_1.edges(">X or <X").fillet(edge_radius)
part_1 = part_1.edges(">Y or <Y").fillet(edge_radius)
part_1 = part_1.edges("|X or <Y").fillet(edge_radius)
part_1 = part_1.edges("|Y").
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2362.stl