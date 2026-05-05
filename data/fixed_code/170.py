import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.3482 * 0.75  # Scaled width
height = 0.0312
inner_length = (0.7187 - 0.0032) * 0.75
inner_width = (0.3972 - 0.0105) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .rect(inner_length, inner_width)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0312, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_170.stl