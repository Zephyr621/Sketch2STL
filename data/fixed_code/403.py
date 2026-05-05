import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.2453 * 0.75  # Scaled width
height = 0.0625
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_403.stl