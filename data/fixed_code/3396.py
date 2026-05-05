import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.5861 * 0.75  # Scaled width
height = 0.1607 + 0.1607
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3333, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Apply rotation and translation ---
assembly = assembly.rotate((0, 0, 0), (0, 0, 1), -90)
assembly = assembly.translate((0, 0.3214, 0))
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
# 导出为STL文件
cq.exporters.export(result, "output_3396.stl