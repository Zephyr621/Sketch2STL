import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.0267 * 0.0536  # Scaled length
width = 0.0536 * 0.0536   # Scaled width
height = 0.0536
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1459, 0.0109, 0.0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
assembly = assembly.rotate((0, 0, 0), (0, 0, 1), -90)
assembly = assembly.translate((0, 0.0536, 0))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2173.stl