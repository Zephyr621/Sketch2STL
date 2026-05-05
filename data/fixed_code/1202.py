import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.2565 * 0.75  # Scaled width
height = 0.0484
part_1 = cq.Workplane("XY").box(length, width, height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0484, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.0484, 0))
# --- Export to STL ---
cq.
# ---
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1202.stl