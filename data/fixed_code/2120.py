import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.0065 * 0.75  # Scaled width
height = 0.0193
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, -0.0193, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
# --- Export to STL ---
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_2120.stl