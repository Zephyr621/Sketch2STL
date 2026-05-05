import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.4896 * 0.75  # Scaled width
height = 0.0225
part_1 = cq.Workplane("XY").rect(length, width).extrude(-height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, -0.0221, 0))
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
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(assembly
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1736.stl