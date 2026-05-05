import cadquery as cq
# --- Part 1: Rectangular Extrusion ---
part_1_width = 0.75 * 0.75  # Scaled width
part_1_length = 0.4091 * 0.75  # Scaled length
part_1_height = 0.0938
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0423, 0))
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
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1379.stl