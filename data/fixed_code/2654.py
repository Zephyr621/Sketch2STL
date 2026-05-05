import cadquery as cq
# --- Part 1: Rectangular Bar ---
length = 0.75 * 0.75  # Scaled length
width = 0.0214 * 0.75  # Scaled width
height = 0.0065
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
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
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2654.stl