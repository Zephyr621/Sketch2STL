import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.6628 * 0.75  # Scaled length
width = 0.3172 * 0.75  # Scaled width
height = 0.0134 * 2  # Total height (both directions)
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0288))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0436, 0))
# --- Export to STL ---
cq.
# --- Export to ST
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2720.stl