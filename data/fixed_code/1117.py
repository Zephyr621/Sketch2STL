import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.0083 * 0.75  # Scaled length
part_1_width = 0.0043 * 0.75  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
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
# --- Export to ST
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1117.stl