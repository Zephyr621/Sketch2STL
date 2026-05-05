import cadquery as cq
# --- Part 1: Rectangular Bar ---
length = 0.75 * 0.75  # Scaled length
width = 0.3643 * 0.75  # Scaled width
height = 0.4245
part_1 = cq.Workplane("XY").rect(length, width).extrude(-height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
#
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3498.stl