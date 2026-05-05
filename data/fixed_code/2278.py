import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.4727 * 0.75  # Scaled width
height = 0.0938 + 0.0938  # Total height (both directions)
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Apply rotation and translation ---
assembly = assembly.rotate((0, 0, 0), (0, 0, 1), -90)
assembly = assembly.translate((0, 0.1875, 0))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2278.stl