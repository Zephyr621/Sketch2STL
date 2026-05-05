import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.0659 * 0.1891  # Scaled length
width = 0.1891 * 0.1891  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)  # Rotate around X axis -90 degrees
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)  # Rotate around Z axis -90 degrees
part_1 = part_1.translate((0.75, 0, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
#
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_832.stl